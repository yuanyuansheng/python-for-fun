from PIL import Image
import numpy as np

a = np.asarray(Image.open(r'/Users/shengyuanyuan/Desktop/golden-gate_web.jpg').convert('L')).astype('float')

depth = 30.  # (0-100)
grad = np.gradient(a)  # Gradient value of the image gray
grad_x, grad_y = grad  # Obtain horizontal and vertical image gradient values respectively
grad_x = grad_x * depth / 100.
grad_y = grad_y * depth / 100.
A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
uni_x = grad_x / A
uni_y = grad_y / A
uni_z = 1. / A

vec_el = np.pi / 2.2  # Top view of light source, radian value
vec_az = np.pi / 4.  # Angle of the light source, the radian value
dx = np.cos(vec_el) * np.cos(vec_az)  # Effect of light on the x-axis
dy = np.cos(vec_el) * np.sin(vec_az)  # Effect of light on the y-axis
dz = np.sin(vec_el)  # Effect of light on the z-axis

b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)  # Light source normalized
b = b.clip(0, 255)

im = Image.fromarray(b.astype('uint8'))  # Reconstruct the image
im.save(r'/Users/shengyuanyuan/Desktop/golden-gate_web.jpg')