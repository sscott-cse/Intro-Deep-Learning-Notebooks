## CSE 479/879 Hackathons

Welcome! This page will host all the hackathons for CSCE 479/879. This README will guide you through getting the Hackathons up and running. Please ask me if you've got any questions or suggestions, and I hope you have a great semester.

### How to Get Started

These instructions are also summarized in [this video](https://github.com/sscott-cse/Intro-Deep-Learning-Notebooks/raw/master/CSCE-479-879/Get-started-with-hackathon-notebook.mp4).  Alternatively, you can utilize Google Colab with help from [this document](https://github.com/sscott-cse/Intro-Deep-Learning-Notebooks/blob/master/CSCE-479-879/using-colab.pdf).  (Note that if you use a resource other than Swan (or some other HCC machine), we cannot provide system-level technical support.)

Before uploading the file to Swan, first download it from GitHub (click to open the file > click the "download raw" button in the upper-right).

To upload a file to Swan
1. Navigate to [swan-ood.unl.edu](https://swan-ood.unl.edu/)
2. In the top drop-down, click the "Files" dropdown and select the "Home Directory" button
3. In the upper right of the page showing the files, click the "Upload" model and use the dialog popup to upload the file.

![Upload Button.png](https://github.com/sscott-cse/Intro-Deep-Learning-Notebooks/blob/d0d364b7072c87487e4014a021a81dfa89c4f81c/2020S_hackathons/Upload%20Button.png)

You can also defer uploading your notebooks until after you have launched Jupyter, and uplaod them directly to your Jupyter working folder. 

### How to Run Hackathons in Jupyter

You can upload each notebook to Swan and run/edit it as you like. To run Jupyter notebooks, go to Interactive Apps > Jupyter Lab.  For now, just accept the default settings, but make sure that the Working Directory is where you uploaded your notebooks (or, launch Jupyter and then upload the notebook).  Make sure you set the kernel to `Python CSE479 (tensorflow-env)` or to your custom kernel. Each hackathon has a homework at the bottom which you should submit to Canvas by the deadline indicated on the Canvas assignment.

Let us know by email, in office hours, or on Piazza if you run into any problems.
![Jupyter Kernel.png](https://github.com/sscott-cse/Intro-Deep-Learning-Notebooks/blob/2774700687fd405c6ddc10dc81cf9c6e3626f912/2020S_hackathons/Jupyter%20Kernel.png)

### Running Outside of Notebooks
To use the environment outside of a Jupyter notebook, you can ssh into Swan and run:
```bash
module load anaconda
conda activate tensorflow-env
```
