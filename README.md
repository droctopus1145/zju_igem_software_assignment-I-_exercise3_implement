<h1 align="center">Octopus Editor</h1>

It's a LLM-drived biological sequence analyzer / editor , integrate ProtBERT to complete missing sequences.

Here is a display video:

<video width="320" height="240" align="center" controls>
   <source src="./image/display.mp4" type="video/mp4">
</video>

<h2>Prerequisites</h2>

need python 3.9+

download these packages

```sh
pip install BioPython
pip install PyQt5
pip install transformers datasets evaluate peft accelerate gradio optimum sentencepiece
pip install jupyterlab scikit-learn pandas matplotlib tensorboard nltk rouge
```

**using a conda virtual environment is highly recommanded**

<h2>Usage</h2>

1. clone the repo:

```sh
git clone https://github.com/droctopus1145/zju_igem_software_assignment-I-_exercise3_implement.git
```

2. activate the conda virtual environment(if you have one)

3. run the code

```sh
python main.py
```

4. to use the ProtBERT , **remember to add a [MASK] tag into the place you want to complete , see the detailed operation in the video

5. enjoy your using