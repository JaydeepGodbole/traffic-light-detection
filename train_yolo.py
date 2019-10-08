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
	pass

if __name__=="__main__":
	#cfg = os.path.join("configs/conf.yaml")
	#logdir = os.path.join('runs', os.path.basename(args.config)[:-4] , str(run_id))
	#writer = SummaryWriter(log_dir=logdir)
	#print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
	print(datetimebeautifier(datetime.now()))
	#print(os.path)