# Rotation
Tools about rotated image </br>
Goals:
- Solve the rotated image out of the boundary.
- Use the center of image to rotate image and resize the new width and height of rotated image.

## Resize rotated image formula
![](https://i.imgur.com/gqdYuNh.png)

reference:
https://iiif.io/api/annex/notes/rotation/

## Start
```python
# Read a image
image = cv2.imread('You_image_path.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
```
Example:</br>
<img src="https://i.imgur.com/YfDENqB.png" width="300" height="300">

```python
# Start rotating
rotated_image = rotate(array=image, angle_in_degrees=30)
plt.imshow(rotated_image)
```
<img src=https://i.imgur.com/618rY0C.png width="300" height="300">

## Problems
There is a problem that needs to solve which is about rotated image with black points.</br>
This is a problem called ''Aliasing''. Multiplying sines and cosines on the integer coordinates of the source image give integers causing some coordinates to be missed completely. The aliasing problem gets worse when angles are closer to the diagonals.</br>

```python=
# rotate.py
# coordinates of pixel of rotated image
new_x, new_y = np.matmul(rotation_matrix, [x,y])
new_y=int(new_centre_height-new_y)
new_x=int(new_centre_width-new_x)
```

![](https://i.imgur.com/LpQZjk8.png)


