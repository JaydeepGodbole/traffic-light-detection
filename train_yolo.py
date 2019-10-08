import os
import sys
import yaml
import time
from datetime import datetime

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models
import torch.optim as optim
from torch.nn.parameter import Parameter
from torch.utils import data
from tensorboardX import SummaryWriter

from helpers.converters import *

def train(cfg, writer, logger):
	

if __name__=="__main__":

	cfg_path = os.path.join(os.getcwd(), "configs", "conf.yaml")
	cfg = yaml.load(cfg_path)
	logdir = os.path.join(os.getcwd(), 'runs', datetimebeautifier(datetime.now()))
	writer = SummaryWriter(log_dir=logdir)
	train(cfg, writer, logger)