import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Danh sách top 10 quốc gia có lượng khách du lịch đến Maldives nhiều nhất
countries = ['China', 'India', 'Russia', 'Germany', 'United Kingdom',
             'Italy', 'United States', 'France']

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Tạo dữ liệu ngẫu nhiên với số lượng khách dao động
np.random.seed(42)
customer_data = pd.DataFrame(np.random.randint(500, 5000, size=(8, 12)), index=countries, columns=months)

# Sắp xếp theo tổng số khách trong năm (giảm dần)
customer_data["Total"] = customer_data.sum(axis=1)
customer_data = customer_data.sort_values(by="Total", ascending=False)
customer_data = customer_data.drop(columns=["Total"])  # Bỏ cột tổng sau khi sắp xếp

# Tạo colormap từ các mã màu mới
custom_cmap = LinearSegmentedColormap.from_list("custom_palette", [
    '#dbdcd7', '#dddcd7', '#e2c9cc', '#e7627d',
    '#b8235a', '#801357', '#3d1635', '#1c1a27'
])

# Vẽ heatmap với bảng màu mới
plt.figure(figsize=(12, 8))
sns.heatmap(customer_data, annot=True, fmt='d', linewidths=.5, cmap=custom_cmap)

plt.title('Top 8 Countries Visiting Maldives Hotels Over 12 Months', fontsize=14)
plt.xlabel('Months', fontsize=12)
plt.ylabel('Country', fontsize=12)
plt.xticks(rotation=45)  # Xoay tên tháng để dễ đọc hơn
plt.show()
