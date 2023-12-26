# PROSPER_app

File explanation

Original App
* app.py: main app file
* requirements.txt: package list
* config.yaml: user list for the app

Others
* Dockerfile: To generate docker image for the app
* app.yaml: app engine setting file (for GCP)
* LICENSE
* README.md: this file

## Description

This is a github repository to develop the PROSPER_app in the streeamlit framework. 


## Installation
```
git clone https://github.com/hirotaka-i/PROSPER_app.git
```

## Create and activate pyenv
please note that the author has the python version of 3.9.6. You can check your version of python by `python --version` or `python3 --version`. If your python version is too old, the package won't work as expected somtimes. If you do not have the right version of python, please install it.

## Set up a virtual environment
To avoid the package dependency problems, we will use virtual environment by running the following command in the terminal.
```
python3 -m venv .venv
```


Then we need to activate the virtual environment which varies depending on your OS.
```
source .venv/bin/activate # Mac
```
```
.venv\Scripts\Activate.ps1 # Windows
```


Please confirm that you have the `(.venv)` in the terminal after activation. Then, update the pip and install the requirement packages in the requirements.txt file.    
```
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Now you are ready to go! Just run 
```
streamlit run app.py
```
The stremalit app will be launched in your browser. If you would like to stop the app, just press `Ctrl + C` in the terminal.

test log in: Username jsmith, password: abc

## Develop the app
You cam modify and edit files in the folder and develop the app. If you would like to add a new package    
```
pip install <package name>
```

If you would like to update the requirements.txt file    
```
pip freeze > requirements.txt
```



if you would like to update your git
```
git add <your updated files>
git commit -m "your comment"
```

You can also connect the folder to your github account or other remote repository. Please refer to the github documentation for more details.

## Deactivate the virtual environment / delete the app
When you finish developing/running the app, please deactivate the virtual environment by running the following command in the terminal.
```
deactivate
```
When you want to come back, you just activate the virtual environment again by running the following command in the terminal. As  you did before.
```
source .venv/bin/activate # Mac
```
```
.venv\Scripts\Activate.ps1 # Windows
```

If you don't need this anymore, just delete the entire folder. 

## Prepare to use Google Cloud Platform
We will use google cloud platform to deploy the app. Please install the google cloud sdk to your computer. Then, run the following command in the terminal.
```
gcloud init
```
or in my case,
```
~/google-cloud-sdk/bin/gcloud init
```
This would enable you to access gcp projects that you created/are invited.


## Dockerize
Now we dockerize the app so that we can deploy it to the cloud. Please install the docker to your computer. Then, run the following command in the terminal. This command automatically look at `Dockerfile` and compose the corresponding Docker image.

```
docker build -t us-east1.gcr.io/prosper1/prospertop:v1 .
```
Please note that I created propser1 project and App Engine was set-up in the us-east1

To test run the docker
```
docker run -p 8081:8080 <IMAGE>
```
Then go to  http://0.0.0.0:8081 to see the app. (8080 was used in my personal computer so changed to 8081)


#### Basic docker function 

```
# list containers
docker ps -a
# remove container
docker rm <CONTAINER_ID>

# list images
docker images
# remove image
docker images rmi <IMAGE>
```

## Deploy
Now deploy the Dockerized app to the App Enging

```
gcloud app deploy app.yaml
```
Or in my case
```
~/google-cloud-sdk/bin/gcloud app deploy app.yaml
```


## Reference
[HOW TO DEPLOY AND SECURE YOUR STREAMLIT APP ON GCP? (artefact)](https://www.artefact.com/blog/how-to-deploy-and-secure-your-streamlit-app-on-gcp/)

## 開発項目

* Authenticatorの日本語化
* 本登録前に同意取得するメカニズム
* 参加登録機能の充実（メールアドレスが同じ場合はリセットにするなど）
* ログイン後画面
* アンケート一覧や回答済みと回答していないアンケートを分けた表示
* アンケートの個別化([参考](https://takeda-san.hatenablog.com/entry/2020/10/24/162454))