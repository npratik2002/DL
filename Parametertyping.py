import tensorflow as tf
from tensorflow.keras.layers import Input, Conv2D, Dense, Flatten
from tensorflow.keras.models import Model

# Define a simple CNN with parameter tying and parameter sharing
def create_shared_cnn(input_shape=(28, 28, 1), num_classes=10):
    # Input layer
    input_layer = Input(shape=input_shape)

    # Shared convolutional layer
    shared_conv_layer = Conv2D(32, kernel_size=(3, 3), activation='relu')

    # Branch 1
    branch1 = shared_conv_layer(input_layer)
    branch1 = Flatten()(branch1)
    branch1 = Dense(64, activation='relu')(branch1)
    output1 = Dense(num_classes, activation='softmax', name='output1')(branch1)

    # Branch 2
    branch2 = shared_conv_layer(input_layer)
    branch2 = Flatten()(branch2)
    branch2 = Dense(64, activation='relu')(branch2)
    output2 = Dense(num_classes, activation='softmax', name='output2')(branch2)

    # Create the model
    model = Model(inputs=input_layer, outputs=[output1, output2])

    return model

# Instantiate the model
shared_cnn_model = create_shared_cnn()

# Compile the model (you can use different loss functions for different outputs)
shared_cnn_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Display the model architecture
shared_cnn_model.summary()
