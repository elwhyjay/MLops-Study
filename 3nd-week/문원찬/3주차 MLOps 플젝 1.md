https://github.com/zademn/mnist-mlops-learning
# 실행
- Streamlit
```
streamlit run frontend/streamlit_main.py
```
- FastAPI
```
uvicorn backend.main:app
```
- MLflow UI (db 있을 때만)
```
mlflow ui --backend-store-uri sqlite:///db/backend.db
```
local tracking (db 없으면 로컬로)
```
mlflow server --host 127.0.0.1 --port 8080
```

# base code 디버깅
### model.py
 - error : model_ 예약어
``` python
model_config = ConfigDict(protected_namespaces=())
```
### main.py
- local tracking
``` python
# mlflow.set_tracking_uri("sqlite:///db/backend.db")
mlflow.set_tracking_uri("http://127.0.0.1:8080")

# model_list = mlflowclient.list_registered_models()
model_list = mlflowclient.search_registered_models()
```
- warning : signature and input example when log model
  크게 상관x
- **stage -> alias**
  안해도 되는듯??
- delete
  model version을 아예 삭제해서 전체 모델이 삭제되도록 수정
# Frontend (Streamlit)
## **streamlit_main.py**
``` python
import streamlit as st
from streamlit_drawable_canvas import st_canvas

import cv2
import requests
import urllib
import json
import os

if page == "Train":
	if st.session_state.model_type == "Linear":
	if st.button("Train"):
	
elif page == "Predict":
	response = requests.get(MODELS_URL)
	if canvas_res.image_data is not None:
	if st.button("Predict"):
	
elif page == "Delete":
	response = requests.get(MODELS_URL)
	if st.button("Delete"):
```
# Backend (FastAPI, mlflow)
## **main.py**
``` python
import numpy as np
from fastapi import FastAPI
from fastapi import BackgroundTasks
from urllib.parse import urlparse
  
import mlflow
# from mlflow.tracking import MlflowClient
from mlflow.client import MlflowClient
from ml.train import Trainer
from ml.models import LinearModel
from ml.data import load_mnist_data
from ml.utils import set_device
from backend.models import DeleteApiData, TrainApiData, PredictApiData

def train_model_task(model_name: str, hyperparams: dict, epochs: int)

@app.get("/")
async def read_root():

@app.get("/models")
async def get_models_api():

@app.post("/train")
async def train_api(data: TrainApiData, background_tasks: BackgroundTasks):

@app.post("/predict")
async def predict_api(data: PredictApiData):

@app.post("/delete")
async def delete_model_api(data: DeleteApiData):

```
## **models.py**
``` python
from typing import Any, Optional, Union
from pydantic import BaseModel, ConfigDict

class TrainApiData(BaseModel):
class PredictApiData(BaseModel):
class DeleteApiData(BaseModel):
```
# ML (MNIST, Linear, Conv)
## **data.py**
``` python
import torch
import torchvision
from torchvision.datasets import MNIST
from torch.utils.data import DataLoader

def load_mnist_data(root='data', flatten=True, batch_size=32)
```
## **models.py**
``` python
import torch
import torchvision

class LinearModel(torch.nn.Module):
	def __init__(self, hyperparameters: dict)
	def forward(self, x)
```
## **train.py**
``` python
import torch
from tqdm import tqdm

class Trainer:
	def __init__(self, model, optimizer=None, criterion=None, device=None)
	def get_model(self)
	def train(self, num_epochs, train_dataloader, val_dataloader=None)
	def train_epoch(self, dataloader)
	def eval_epoch(self, dataloader)
```
## **utils.py**
``` python
import torch

def set_device(cuda: bool = True)
```

# CNN 추가
