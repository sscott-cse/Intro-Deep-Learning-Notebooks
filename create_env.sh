module purge
module load tensorflow-gpu/py39/2.6
module load anaconda
conda create -p /work/cse479/shared/envs/tensorflow-env --clone $CONDA_DEFAULT_ENV
module unload tensorflow-gpu/py39/2.6
conda activate /work/cse479/shared/envs/tensorflow-env
conda install --freeze-installed tensorflow-datasets tqdm matplotlib ipywidgets gym scipy tensorflow-hub
# Install ipykernel
conda install ipykernel
# Install the kernel specification
python -m ipykernel install --user --name "$CONDA_DEFAULT_ENV" --display-name "Python CSE479 ($CONDA_DEFAULT_ENV)"
