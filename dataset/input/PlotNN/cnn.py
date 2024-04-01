from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Activation

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),  # 卷积层
    MaxPooling2D((2, 2)),  # 池化层
    Conv2D(64, (3, 3), activation='relu'),  # 另一个卷积层
    MaxPooling2D((2, 2)),  # 另一个池化层
    Flatten(),  # 展平层，为全连接层准备
    Dense(64, activation='relu'),  # 全连接层
    Dense(10, activation='softmax')  # 输出层，假设为10类分类
])

model.summary()  # 查看模型结构
