# Image Recognition Server

Image Recognition is a server written in Python which uses Python ImageAI module.  After you install and run it, you can send a POST request with a image file you want to recognize and get JSON response. You can test the server using built-in HTML form.

This program requires:
- Python 3.*
- pip3

# Install

 Install all ImageAI dependencies
#### Tensorflow
 
 ```sh
pip3 install --upgrade tensorflow
```

#### Numpy
 ```sh
pip3 install numpy
```

#### SciPy
 ```sh
pip3 install scipy
```

#### OpenCV
 ```sh
pip3 install opencv-python
```

#### Matplotlib
 ```sh
pip3 install matplotlib
```

#### h5py
 ```sh
pip3 install h5py
```

#### Keras
 ```sh
pip3 install keras
```

#### Install the special library for ImageAI
 ```sh
pip3 install https://github.com/OlafenwaMoses/ImageAI/raw/master/dist/imageai-1.0.2-py3-none-any.whl
```



# Install ImageRecognitionServer
```sh
git clone https://github.com/alkhachatryan/image_recognition.git
cd image_recognition
chmod +x server.py
```

# Run the server
```sh
 ./server.py
 # starting server...
 # running server on http://127.0.0.1:8081...
 
  # Send Image with 'file' key to this address and get JSON back
```

# References
OlafenwaMoses/ImageAI
https://github.com/OlafenwaMoses/ImageAI

# License
https://github.com/alkhachatryan/image_recognition/blob/master/LICENSE