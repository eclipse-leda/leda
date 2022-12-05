---
title: "GitHub Workflow"
date: 2022-05-09T14:24:56+05:30
weight: 5
---

![GitHub Workflow](./github-workflow.png)

- Manually creating a Release triggers the release workflow.
- The release workflow calls the build workflow.
- The build workflow indirectly depends on the sstate cache being prebuilt manually (see optimizations below)
- The build workflow runs a full build of the SDV-Image-All disk image for all target machines.
- A separate job is used for each target machine, to ensure an image build for a target machine can finish within 6 hours.
- Each build contains the creation of SBOM artifacts and the check for CVEs. The SBOM artifacts are in SPDX JSON format and packaged per target machine's disk image (SDV-Image-Full to include all packages).
- The OSS License Scanning (using the OSS Review Toolkit) is done asynchronously on a separate fork, as it currently uses a proprietary infrastructure. The ORT-based infrastructure of Eclipse is planned to be used in the future. The web report is attached as a build artifact on the internal fork and not accessible by public currently.
- Once the build workflow's jobs are finished, the release workflow will finalize by attaching the release artifacts as assets to the release. 

*Note: While the build workflow and release workflows are in progress, the GitHub release page of that release does not show any other assets besides the source archives. The release artifacts (eclipse-leda-<machine>.tar.xz) will only be visible once all workflows have finished.*

## Limitations on standard runners

As the GitHub-managed runners are optimized for ephemeral build use cases and a Yocto-based build process is very consuming in regards to CPU and disk capacity, a few optimizations need to be done before being able to run a full build or even a release workflow on limited GitHub-managed standard runners.

Please see the documentation about [GitHub Hosted Runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners#supported-runners-and-hardware-resources) for current specs.

| Resource  | Standard GitHub Runner | Recommended for Yocto |
|---|---|---|
| CPU | 2-core CPU (x86_64) | 16-core CPU (x86_64) |
| RAM | 7 GB of RAM  | 16 GB of RAM |
| Disk | 14 GB of SSD  | 128+ GB of SSD |
| Time | max. 6 hours / job  | not limited |

In general, GitHub recommends to split a build process into smaller chunks, which can then fit into the constraints.

## Optimizations

The following optimizations have been implemented for the Eclipse Leda public repository and its build workflow:

1. **Remote SState Cache**: To minimize build time and disk usage, a remote sstate-cache mirror is being used. The mirror is hosted by one of the project sponsors on european Azure infrastructure and available as public HTTP mirror to anonymous Leda builds. The mirror is provided as best-effort, does not provide any kind of service level and may not be available at all times.

   *Note: To use the mirror, set the `BB_HASHSERVE`, `MIRROR_SERVER`, `SSTATE_MIRRORS` and related configuration settings. See the [mirrors.yaml](https://github.com/eclipse-leda/leda-distro/blob/main/kas/mirrors.yaml) for a full sample.*
    
   ![GitHub Workflow Optimizations](./github-workflow-optimizations.png)

2. **Prebuilding**: To fill the remote sstate cache mirror, another build infrastructure is being used. The repository fork has been configured with additional credentials to authenticate against the remote mirror for uploading the built packages. To ensure these steps are not run on the public OSS repository, the workflow steps use additional conditions to check for the owner of the repository. This is a workaround due to a [known issue on GitHub Actions](https://github.com/actions/runner/issues/520).

2. **Chunking of the build steps:** To minimize bandwidth transfer, a local GitHub Action Cache is being used. This cache is per target machine and filled with a separate workflow. The [Prebuild sstate](https://github.com/eclipse-leda/leda-distro/actions/workflows/prebuild-sstate.yml) build jobs will run the BitBake process for 4 hours and then gracefully shut down. The build process will finish the current tasks. The remaining time (max. runtime for GitHub Runners is 6 hours) is used to package and upload the packages to the cache. If the 4 hours of build time are not enough, it may be required to re-run the same job more often.

   *Note: The disadvantage of this approach is that each run requires a significant lead time where the remote cache is downloaded, the recipes get parsed again, the build task dependencies are compiled etc. On a persistent runner, this time can be spared.*

3. **Rerun on sstate miss:** When BitBake is missing a package in the sstate mirror (it may exist in the Hash Equivalence Server though), BitBake will log an **Error** and continue to run the recipe. However, as the cache-miss is logged as error, BitBake will exit with an error code, indicating a failed build, which in turn would mark the GitHub Job as failed, too. To circumvent this problem, the BitBake build process is executed in a loop (max. 3 retries) to ensure that with the current state, all packages can be built without errors, eventually succeeding with the buid.

4. **Always upload GitHub Cache:** Under normal circumstances, the GitHub Cache action will update the cache on success of the build job - to not poison the cache with failed builds. However, as the Leda build workflows run for a very long time and may fail due to other reasons, the goal is to still reuse the sstate-cache as much as possible. For that reason, the `pat-s/always-upload-cache` GitHub action is being used, as it will also upload the cache on failed builds.

