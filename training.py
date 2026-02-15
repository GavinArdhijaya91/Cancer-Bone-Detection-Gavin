import tensorflow as tf
from tensorflow import keras
layers = keras.layers
models = keras.models

train_ds = tf.keras.utils.image_dataset_from_directory('dataset/train', image_size=(224, 224),
batch_size=32, label_mode='binary'
)

base_model = tf.keras.applications.ResNet50(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet'
)
base_model.trainable = False

model = models.Sequential([
    layers.Input(shape=(224, 224, 3)),
    layers.Rescaling(1./255),
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.4), 
    layers.Dense(1, activation='sigmoid') 
])

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
    loss='binary_crossentropy', 
    metrics=['accuracy']
)
model.fit(train_ds, epochs=10)

model.save('model/trained_modelff.h5')
print("Model berhasil disimpan di folder model/")