from pathlib import Path
from typing import Optional, Dict

from phidata.base import PhidataBase, PhidataBaseArgs
from phidata.infra.docker.resource.group import (
    DockerResourceGroup,
    DockerBuildContext,
)
from phidata.infra.k8s.resource.group import (
    K8sResourceGroup,
    K8sBuildContext,
)
from phidata.utils.log import logger


class PhidataAppArgs(PhidataBaseArgs):
    name: str

    # If True, skip resource creation if active resources with the same name exist.
    use_cache: bool = True

    # Parameters populated during K8sWorker.init_resources()
    # These are passed down from the WorkspaceConfig -> K8sConfig -> K8sArgs -> PhidataApp
    # -*- Path parameters
    # Path to the workspace root directory
    workspace_root_path: Optional[Path] = None
    # Path to the workspace config file
    workspace_config_file_path: Optional[Path] = None
    # Path to important directories relative to the workspace_root
    # These directories are joined to the workspace_root dir
    #   to build paths depending on the environments (local, docker, k8s)
    # defaults are set by WorkspaceConfig.__init__()
    scripts_dir: Optional[str] = None
    storage_dir: Optional[str] = None
    meta_dir: Optional[str] = None
    products_dir: Optional[str] = None
    notebooks_dir: Optional[str] = None
    workspace_config_dir: Optional[str] = None

    # -*- Environment parameters
    # Env vars added to docker env when building PhidataApps
    #   and running workflows
    docker_env: Optional[Dict[str, str]] = None
    # Env vars added to k8s env when building PhidataApps
    #   and running workflows
    k8s_env: Optional[Dict[str, str]] = None

    # -*- AWS parameters
    # Common aws params used by apps, resources and data assets
    aws_region: Optional[str] = None
    aws_profile: Optional[str] = None
    aws_config_file: Optional[str] = None
    aws_shared_credentials_file: Optional[str] = None

    # These are passed down from the K8sConfig -> K8sArgs -> PhidataApp
    # K8s namespace to use
    namespace: str = "default"
    # K8s context to use
    context: Optional[str] = None
    # K8s service account to use
    service_account_name: Optional[str] = None
    # Common K8s labels to add to all resources
    common_labels: Optional[Dict[str, str]] = None

    class Config:
        arbitrary_types_allowed = True


class PhidataApp(PhidataBase):
    """Base Class for all PhidataApps"""

    def __init__(self) -> None:
        super().__init__()
        self.args: Optional[PhidataAppArgs] = None
        self.docker_resource_groups: Optional[Dict[str, DockerResourceGroup]] = None
        self.k8s_resource_groups: Optional[Dict[str, K8sResourceGroup]] = None

    @property
    def workspace_root_path(self) -> Optional[Path]:
        return self.args.workspace_root_path if self.args else None

    @workspace_root_path.setter
    def workspace_root_path(self, workspace_root_path: Path) -> None:
        if self.args is not None and workspace_root_path is not None:
            self.args.workspace_root_path = workspace_root_path

    @property
    def workspace_config_file_path(self) -> Optional[Path]:
        return self.args.workspace_config_file_path if self.args else None

    @workspace_config_file_path.setter
    def workspace_config_file_path(self, workspace_config_file_path: Path) -> None:
        if self.args is not None and workspace_config_file_path is not None:
            self.args.workspace_config_file_path = workspace_config_file_path

    @property
    def scripts_dir(self) -> Optional[str]:
        return self.args.scripts_dir if self.args else None

    @scripts_dir.setter
    def scripts_dir(self, scripts_dir: str) -> None:
        if self.args is not None and scripts_dir is not None:
            self.args.scripts_dir = scripts_dir

    @property
    def storage_dir(self) -> Optional[str]:
        return self.args.storage_dir if self.args else None

    @storage_dir.setter
    def storage_dir(self, storage_dir: str) -> None:
        if self.args is not None and storage_dir is not None:
            self.args.storage_dir = storage_dir

    @property
    def meta_dir(self) -> Optional[str]:
        return self.args.meta_dir if self.args else None

    @meta_dir.setter
    def meta_dir(self, meta_dir: str) -> None:
        if self.args is not None and meta_dir is not None:
            self.args.meta_dir = meta_dir

    @property
    def products_dir(self) -> Optional[str]:
        return self.args.products_dir if self.args else None

    @products_dir.setter
    def products_dir(self, products_dir: str) -> None:
        if self.args is not None and products_dir is not None:
            self.args.products_dir = products_dir

    @property
    def notebooks_dir(self) -> Optional[str]:
        return self.args.notebooks_dir if self.args else None

    @notebooks_dir.setter
    def notebooks_dir(self, notebooks_dir: str) -> None:
        if self.args is not None and notebooks_dir is not None:
            self.args.notebooks_dir = notebooks_dir

    @property
    def workspace_config_dir(self) -> Optional[str]:
        return self.args.workspace_config_dir if self.args else None

    @workspace_config_dir.setter
    def workspace_config_dir(self, workspace_config_dir: str) -> None:
        if self.args is not None and workspace_config_dir is not None:
            self.args.workspace_config_dir = workspace_config_dir

    @property
    def docker_env(self) -> Optional[Dict[str, str]]:
        return self.args.docker_env if self.args else None

    @docker_env.setter
    def docker_env(self, docker_env: Dict[str, str]) -> None:
        if self.args is not None and docker_env is not None:
            self.args.docker_env = docker_env

    @property
    def k8s_env(self) -> Optional[Dict[str, str]]:
        return self.args.k8s_env if self.args else None

    @k8s_env.setter
    def k8s_env(self, k8s_env: Dict[str, str]) -> None:
        if self.args is not None and k8s_env is not None:
            self.args.k8s_env = k8s_env

    @property
    def aws_region(self) -> Optional[str]:
        return self.args.aws_region if self.args else None

    @aws_region.setter
    def aws_region(self, aws_region: str) -> None:
        if self.args is not None and aws_region is not None:
            self.args.aws_region = aws_region

    @property
    def aws_profile(self) -> Optional[str]:
        return self.args.aws_profile if self.args else None

    @aws_profile.setter
    def aws_profile(self, aws_profile: str) -> None:
        if self.args is not None and aws_profile is not None:
            self.args.aws_profile = aws_profile

    @property
    def aws_config_file(self) -> Optional[str]:
        return self.args.aws_config_file if self.args else None

    @aws_config_file.setter
    def aws_config_file(self, aws_config_file: str) -> None:
        if self.args is not None and aws_config_file is not None:
            self.args.aws_config_file = aws_config_file

    @property
    def aws_shared_credentials_file(self) -> Optional[str]:
        return self.args.aws_shared_credentials_file if self.args else None

    @aws_shared_credentials_file.setter
    def aws_shared_credentials_file(self, aws_shared_credentials_file: str) -> None:
        if self.args is not None and aws_shared_credentials_file is not None:
            self.args.aws_shared_credentials_file = aws_shared_credentials_file

    @property
    def namespace(self) -> Optional[str]:
        return self.args.namespace if self.args else None

    @namespace.setter
    def namespace(self, namespace: str) -> None:
        if self.args is not None and namespace is not None:
            self.args.namespace = namespace

    @property
    def context(self) -> Optional[str]:
        return self.args.context if self.args else None

    @context.setter
    def context(self, context: str) -> None:
        if self.args is not None and context is not None:
            self.args.context = context

    @property
    def service_account_name(self) -> Optional[str]:
        return self.args.service_account_name if self.args else None

    @service_account_name.setter
    def service_account_name(self, service_account_name: str) -> None:
        if self.args is not None and service_account_name is not None:
            self.args.service_account_name = service_account_name

    @property
    def common_labels(self) -> Optional[Dict[str, str]]:
        return self.args.common_labels if self.args else None

    @common_labels.setter
    def common_labels(self, common_labels: Dict[str, str]) -> None:
        if self.args is not None and common_labels is not None:
            self.args.common_labels = common_labels

    ######################################################
    ## DockerResourceGroup
    ######################################################

    def init_docker_resource_groups(
        self, docker_build_context: DockerBuildContext
    ) -> None:
        logger.debug(
            f"@init_docker_resource_groups not defined for {self.__class__.__name__}"
        )

    def get_docker_resource_groups(
        self, docker_build_context: DockerBuildContext
    ) -> Optional[Dict[str, DockerResourceGroup]]:
        if self.docker_resource_groups is None:
            self.init_docker_resource_groups(docker_build_context)
        # # Comment out in prod
        # if self.docker_resource_groups:
        #     logger.debug("DockerResourceGroups:")
        #     for rg_name, rg in self.docker_resource_groups.items():
        #         logger.debug(
        #             "{}: {}".format(rg_name, rg.json(exclude_none=True, indent=2))
        #         )
        return self.docker_resource_groups

    ######################################################
    ## K8sResourceGroup
    ######################################################

    def init_k8s_resource_groups(self, k8s_build_context: K8sBuildContext) -> None:
        logger.debug(
            f"@init_docker_resource_groups not defined for {self.__class__.__name__}"
        )

    def get_k8s_resource_groups(
        self, k8s_build_context: K8sBuildContext
    ) -> Optional[Dict[str, K8sResourceGroup]]:
        if self.k8s_resource_groups is None:
            self.init_k8s_resource_groups(k8s_build_context)
        # # Comment out in prod
        # if self.k8s_resource_groups:
        #     logger.debug("K8sResourceGroups:")
        #     for rg_name, rg in self.k8s_resource_groups.items():
        #         logger.debug(
        #             "{}:{}\n{}".format(rg_name, type(rg), rg)
        #         )
        return self.k8s_resource_groups
