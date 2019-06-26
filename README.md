# Learning to See 

![](challenge/graphics/finger_counting_demo.gif)

## About 
This repository supports the YouTube series [Learning to See](https://www.youtube.com/watch?v=i8D90DkCLhI&list=PLiaHhY2iBX9ihLasvE8BKnS2Xg8AhY6iV). We'll take a bottom-up appraoch to machine learning for computer vision, and tackle one problem: counting the number of fingers in an image from a [Leap Motion](https://www.leapmotion.com/) Infared Camera.

## Lectures
| Order |   Notebook/Slides  | Topic | Required Viewing Before | Additional Reading | Notes |
| ----- | ------------------ | ------ | ----------------------- | ------------------ | ----- |
| 1 | [Rules](https://github.com/unccv/learning_to_see/blob/master/notebooks/1-Rules.ipynb) | Let's try a rules based approach to real CV problem | [LTS part 1](https://www.youtube.com/watch?v=i8D90DkCLhI&list=PLiaHhY2iBX9ihLasvE8BKnS2Xg8AhY6iV) | - | [Intro to Programming Challenge](https://github.com/unccv/learning_to_see/blob/master/challenge/challenge_instructions.ipynb) |
| 2 | [Machine Learning](https://github.com/unccv/learning_to_see/blob/master/notebooks/2-Machine%20Learning.ipynb) | Can we learn a better way from data? | [LTS part 2, 3](https://www.youtube.com/watch?v=2ZhQkD1QKFw&index=2&list=PLiaHhY2iBX9ihLasvE8BKnS2Xg8AhY6iV) | - | - |
| 3 | [Generalization](https://github.com/unccv/learning_to_see/blob/master/notebooks/3-Generalization%20and%20Legos.ipynb) | How do we know if our models are actually working? | [LTS part 4, 5](https://www.youtube.com/watch?v=sarVw-iVWgc&index=4&list=PLiaHhY2iBX9ihLasvE8BKnS2Xg8AhY6iV) | [Surely You're Joking Mr. Feynman](https://www.amazon.com/Surely-Youre-Joking-Mr-Feynman-ebook/dp/B003V1WXKU/ref=sr_1_1?ie=UTF8&qid=1530909477&sr=8-1&keywords=surely+you%27re+joking+mr.+feynman) | - |
| 4 | [Learning From Data](https://github.com/unccv/learning_to_see/blob/master/slides/learning_from_data.pptx) | But how do we really know that our models are working? | [LTS part 6, 7](https://www.youtube.com/watch?v=GufQYkMkdpw&index=6&list=PLiaHhY2iBX9ihLasvE8BKnS2Xg8AhY6iV) | - | [Caltec Learning From Data Lecture 2](https://www.youtube.com/watch?v=MEG35RDD7RA&hd=1)|
| 5 | [Simple Rules](https://github.com/unccv/learning_to_see/blob/master/slides/simple_rules.pptx) | Why should we prefer simple rules? | [LTS part 8, 9](https://www.youtube.com/watch?v=UVwwYZMFocg) | [Caltec Learning From Data Lecture 2](https://www.youtube.com/watch?v=MEG35RDD7RA&hd=1)| - | 
| 6 | [Decision Trees](https://github.com/unccv/learning_to_see/blob/master/slides/decision_trees.pptx) | How do we actually find good rules? | [LTS part 10-15](https://www.youtube.com/watch?v=6cvPj9dmYTo) | [hackerdashery P vs NP](https://www.youtube.com/watch?v=YX40hbAHx3s)| - |

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

### Launching the Jupyter Notebooks
To properly view the images and animations, please launch your jupyter notebook from the root directory of this repository. 

### Graphviz on Windows
Windows users may need to install GraphViz separetely if you are getting [GraphViz's executables not found](https://stackoverflow.com/questions/18438997/why-is-pydot-unable-to-find-graphvizs-executables-in-windows-8) exception in notebook 4.
1. [Download GraphViz MSI](https://graphviz.gitlab.io/_pages/Download/Download_windows.html)
2. Add "C:\Program Files (x86)\Graphviz2.34\bin\" to your PATH variable.
3. Stop/Exit your current python environment/IDE and start again.


   
