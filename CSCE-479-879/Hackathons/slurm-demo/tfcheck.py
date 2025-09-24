import tensorflow as tf
import numpy as np
from transformers import TFT5ForConditionalGeneration, T5Tokenizer

print("SLURM DEMO") # sbatch submit_gpu.sh python tfcheck.py

print("Num GPUs Available:", len(tf.config.list_physical_devices('GPU')))
print("TensorFlow version:", tf.__version__)
print("Built with CUDA:", tf.test.is_built_with_cuda())
print("Built with GPU support:", tf.test.is_built_with_gpu_support())


print("*"*100)
print("Testing T5-small")

# Load tokenizer and TF model
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = TFT5ForConditionalGeneration.from_pretrained(model_name)

# Encode input text
input_text = "summarize: The quick brown fox jumps over the lazy dog. This sentence is often used to test typing speed and display fonts."
input_ids = tokenizer(input_text, return_tensors="tf").input_ids

# Generate output
outputs = model.generate(input_ids, max_length=40, num_beams=4, early_stopping=True)

# Decode prediction
print(tokenizer.decode(outputs[0], skip_special_tokens=True))

# =============================================================================================================================

print("-"*100)

# a 0-dim tensor; a scalar with shape ()
# note that double precision (64 bits) is 
#     not necessary in deep learning
its_complicated = tf.convert_to_tensor(12.3 - 4.85j, tf.complex64)
print(its_complicated)
print()

# a 1-dim tensor; a vector with shape (5,), meaning it's just a plain 'ol array
# notice that we've given a name to this variable
first_primes = tf.convert_to_tensor(np.array([2, 3, 5, 7, 11], np.int32), name="primes")
print(first_primes)
print()

# a 2-dim tensor; a matrix with shape [2, 3]
# notice that the dtype is inferred when we don't specify it
my_identity = tf.ones([2, 3])
print(my_identity)
print(
    "We can retrieve a numpy array from TensorFlow:",
    my_identity.numpy(),
    "is a",
    type(my_identity.numpy()),
)
print()

# a 4-dim tensor with shape [10, 299, 299, 3]
blank_image = tf.zeros([10, 299, 299, 3])
print("tf.shape returns a Tensor:", tf.shape(blank_image))
print("while .shape returns a tuple:", blank_image.shape)

print("FIN")