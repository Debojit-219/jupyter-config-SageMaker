# Configuration file for jupyter-notebook.

c = get_config()  #noqa

## The default URL to redirect to from `/`
# Default: '/notebooks/Untitled.ipynb'
c.NotebookApp.default_url = '/notebooks/Untitled.ipynb'


c.NotebookApp.kernel_spec_manager_class = 'environment_kernels.EnvironmentKernelSpecManager'
c.NotebookApp.iopub_data_rate_limit = 10000000000