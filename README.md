# Learning to See 

![](challenge/graphics/finger_counting_demo.gif)


## About 
This repository supports the YouTube series [Learning to See](https://www.youtube.com/watch?v=i8D90DkCLhI&list=PLiaHhY2iBX9ihLasvE8BKnS2Xg8AhY6iV). We'll take a bottom-up appraoch to machine learning for computer vision, and tackle one problem: counting the number of fingers in an image from a [Leap Motion](https://www.leapmotion.com/) Infared Camera.


### Note on Launching the Jupyter Notebooks
To properly view the images and animations, please launch your jupyter notebook from the root directory of this repository. 

## Setup 

The Python 3 [Anaconda Distribution](https://www.anaconda.com/download) is the easiest way to get going with the notebooks and code presented here. 

(Optional) You may want to create a virtual environment for this repository: 

~~~
conda create -n cv python=3 
source activate cv
~~~

You'll need to install the jupyter notebook to run the notebooks:

~~~
conda install jupyter

# You may also want to install nb_conda (Enables some nice things like change virtual environments within the notebook)
conda install nb_conda
~~~

This repository requires the installation of a few extra packages, you can install them all at once with:
~~~
pip install -r requirements.txt
~~~

(Optional) [jupyterthemes](https://github.com/dunovank/jupyter-themes) can be nice when presenting notebooks, as it offers some cleaner visual themes than the stock notebook, and makes it easy to adjust the default font size for code, markdown, etc. You can install with pip: 

~~~
pip install jupyterthemes
~~~

Recommend jupyter them for **presenting** these notebook (type into terminal before launching notebook):
~~~
jt -t grade3 -cellw=90% -fs=20 -tfs=20 -ofs=20 -dfs=20
~~~

Recommend jupyter them for **viewing** these notebook (type into terminal before launching notebook):
~~~
jt -t grade3 -cellw=90% -fs=14 -tfs=14 -ofs=14 -dfs=14
~~~

## Notes  
Windows users may need to install GraphViz separetely if you are getting [GraphViz's executables not found](https://stackoverflow.com/questions/18438997/why-is-pydot-unable-to-find-graphvizs-executables-in-windows-8) exception in notebook 4.
1. [Download GraphViz MSI](https://graphviz.gitlab.io/_pages/Download/Download_windows.html)
2. Add "C:\Program Files (x86)\Graphviz2.34\bin\" to your PATH variable.
3. Stop/Exit your current python environment/IDE and start again.


   
