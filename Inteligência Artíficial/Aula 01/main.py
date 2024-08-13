import tensorflow as tf
predicted_probs = tf.constant([0.9, 0.2])
true_labels = tf.cnstant({1.0, 0.0})
loss = tf.keras.losses.binary_crossentropy(true_labels, predicted_probs)
print("Binary Cross-Entropy Loss: ", loss.numpy())