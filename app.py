# Import packages.

# Create a Flask app.

# Set the model directory.

classes = [ "Sakura", "Jiraiya", "Sasuke" ]

# Create the index route.
def index():

# Create the predict route and accept POST requests.
def predict():
    temp_image_name = "temp_image.png"

    request.files["upload-image"].save(temp_image_name)

    upload_image = tf.keras.preprocessing.image.load_img(temp_image_name, target_size = (224, 224))

    os.remove(temp_image_name)

    preprocessed_image = np.expand_dims(tf.keras.preprocessing.image.img_to_array(upload_image) / 255., axis = 0)

    base_model = tf.keras.applications.resnet50.ResNet50(weights = None, include_top = False)

    x = base_model.output
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dense(512, activation = "relu")(x)
    x = tf.keras.layers.Dropout(0.6)(x)

    model = tf.keras.models.Model(inputs = base_model.input, outputs = tf.keras.layers.Dense(len(classes), activation = "softmax")(x))

    model.load_weights() # load the selected model

    # Get the predicted class and render the predict.html webpage.

# Run the app.
