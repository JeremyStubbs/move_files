import os
import shutil
import random
import glob

os.chdir('data/dogs-vs-cats')
if os.path.isdir('train/dog') is False:
  os.makedir('train/dog')
  os.makedir('train/cat')
  os.makedir('valid/dog')
  os.makedir('valid/cat')
  os.makedir('test/dog')
  os.makedir('test/cat')

  for c in random.sample(glob.glob('cat*'), 500):
    shutil.move(c, 'train/cat')
  for c in random.sample(glob.glob('dog*'), 500):
    shutil.move(c, 'train/dog')
  for c in random.sample(glob.glob('cat*'), 100):
    shutil.move(c, 'valid/cat')
  for c in random.sample(glob.glob('dog*'), 100):
    shutil.move(c, 'valid/dog')
  for c in random.sample(glob.glob('cat*'), 50):
    shutil.move(c, 'test/cat')
  for c in random.sample(glob.glob('dog*'), 50):
    shutil.move(c, 'test/dog')

os.chdir('../../')