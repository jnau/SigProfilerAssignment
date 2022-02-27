from setuptools import setup
import shutil
import os
import sys
import subprocess

#remove the dist folder first if exists
if os.path.exists("dist"):
    shutil.rmtree("dist")

VERSION = '0.1.0'


with open('README.md') as f:
	long_description = f.read()

def write_version_py(filename='SigProfilerSingleSamplePro/version.py'):
    # Copied from numpy setup.py
    cnt = """
# THIS FILE IS GENERATED FROM SigProfilerSingleSamplePro SETUP.PY
short_version = '%(version)s'
version = '%(version)s'
Update = 'Heirarchy option deleted, clustering deleted and signatures orders by the mutation burden'
    
    """
    fh = open(filename, 'w')
    fh.write(cnt % {'version': VERSION,})
    fh.close()
requirements=[
          'scipy>=1.6.3',
          'numpy>=1.21.2',
          'pandas>=1.2.4', 
          'SigProfilerExtractor>=1.1.4',
          'SigProfilerMatrixGenerator>=1.1.30', 
          'sigProfilerPlotting>=1.1.15', 
          'pillow',
          'statsmodels>=0.9.0',
          'scikit-learn>=0.24.2',
          'psutil>=5.6.1',
          'reportlab>=3.5.42',
          'PyPDF2>=1.26.0'
           ]

# operating_system = sys.platform   
# print(operating_system)
# if operating_system  in ['win32','cygwin','windows']:
#     requirements.remove('matplotlib>=3.3.0')
#     requirements.remove('torch==1.5.1')
#     print('Trying to install pytorch!')
#     code = 1
#     try:
#         code = subprocess.call(['pip', 'install', 'torch===1.5.1+cpu',  '-f', 'https://download.pytorch.org/whl/torch_stable.html'])
#         if code != 0:
#             raise Exception('Torch  instalation failed !')
#     except:
#         try:
#             code = subprocess.call(['pip3', 'install', 'torch===1.5.1+cpu',  '-f', 'https://download.pytorch.org/whl/torch_stable.html'])
#             if code != 0:
#                 raise Exception('Torch instalation failed !')
#         except:
#             print('Failed to install pytroch, please install pytroch manually be following the simple instructions over at: https://pytorch.org/get-started/locally/')
#     if code == 0:
#         print('Successfully installed pytorch version! (If you need the GPU version, please install it manually, checkout the mindsdb docs and the pytroch docs if you need help)')
    
    
write_version_py()
setup(name='SigProfilerSingleSamplePro',
      version=VERSION,
      description='Decompose Denovo solutions to Signature Databases',
      long_description=long_description,
      long_description_content_type='text/markdown',  # This is important!	
      url="https://github.com/AlexandrovLab/SigProfilerSingleSamplePro.git",
      author='Raviteja Vangara',
      author_email='rvangara@ucsd.edu',
      license='UCSD',
      packages=['SigProfilerSingleSamplePro'],
      install_requires=requirements,
      include_package_data=True,      
      zip_safe=False)