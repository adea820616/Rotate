# Rotate
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
Example:
![](https://i.imgur.com/YfDENqB.png =300x300)

```python
# Start rotating
rotated_image = rotate(array=image, angle_in_degrees=30)
plt.imshow(rotated_image)
```
![](https://i.imgur.com/618rY0C.png =300x300)

## Problems
There is a problem that needs to solve which is about rotated image with black points.

![](https://i.imgur.com/LpQZjk8.png)


