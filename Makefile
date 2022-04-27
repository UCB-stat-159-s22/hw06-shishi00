.PHONY: env
env: 
  conda env create -f environment.yml --name ligo
  conda activate ligo
  python -m ipykernel install --user --name=ligo
 
.PHONY: html
html:
  jupyter-book build .
  
.PHONY: html-hub
html-hub:
  jupyter-book config sphinx .
  sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
  @echo "go to this url https://stat159.datahub.berkeley.edu/user-redirect/proxy/8000/index.html" 
  
.PHONY: clean
clean:
  rm -f figures/*.png
  rm -f audio/*.wav
  rm -f data/*.csv
  rm -rf build/*
  
