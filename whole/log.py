import pickle

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys

from networkx import read_multiline_adjlist
from streamlit.components.v1 import html

from streamlit_option_menu import option_menu

import creat as ct
import generated_data as gd
import itemsyle_all as item

import streamlit as st

st.text_input('请输入你的用户名:')
st.text_input('请输入密码:')