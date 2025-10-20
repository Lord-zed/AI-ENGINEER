
# IMPORT
#url = "https://raw.githubusercontent.com/username/repository/branch/path/to/yourfile.csv"
#df = pd.read_csv(url)
sales=pd.read_csv('sales_data.xls')

# EDA ******
len(sales.columns)

# using loc and iloc
sales.loc[[0,2,4,6]]  # works with both integres and strings
sales.iloc[[0,2,4,6]] # works with only integers

# indexing column using loc. this is having first argument for the row and second argument column using column names or strings
sales.loc[[0,2,4,6], ['customer_id','device_id','item_id']]

# indexing columns by having first argument for the row and the second argument for the column but taking the index number
sales.iloc[[0,2,4,6],[0,1,2,10]]

# lets work with index...using loc and iloc... SETTING INDEX
sales.set_index("location", inplace = True)
sales.index

# list af all the locations or countries where all the customers purchase from...
unique_index = sales.index.unique().sort_values()
unique_index
unique_index.nunique()

# top 10 countries or locations where most patronage are recieved...
sales.index.value_counts()
# bar chat plot of index
sales.index.value_counts().head(10).plot(kind = 'bar')

sales.loc["Brazil"] # I selected any of the unique values in the index...

# FILTERING *******
sales[sales["customer_id"] == "56d7d069-2f58-4b35-9559-9405c45cae33"]

# Total nmunbers of customers
sales["customer_id"].nunique()

# Top 20 custommers with the highest purchases....
sales["customer_id"].value_counts().sort_values(ascending = False).head(20).plot(kind="bar")

# lets pick one of these customers and see their behaviour
mask = (sales["customer_id"] == "ebcb2343-be1b-421e-83eb-6f79a321d999")

sales.loc[mask,"customer_id":"currency"].head(2) # give me mask , but from colunm customer_id to currency

sales["currency"].nunique()
sales["currency"].unique()

currency_and_number_times_used = sales["currency"].value_counts()
currency_and_number_times_used

# plotting bar 
currency_and_number_times_used.plot(kind ="bar" )

# USING MULTIPLE FILTER
mask2 = (sales["customer_id"] == "ebcb2343-be1b-421e-83eb-6f79a321d999") & (sales["status"] == "success")

# lets see the numbers of sucessful transaction carried out by this customer
this_customer = sales.loc[mask]

this_customer["status"].value_counts()
# The output showsthat the particular customer has not experienced failed transaction  at all.

# LEts find out the numbers of failed transaction as compared to others...
transaction_status = sales["status"].value_counts()
transaction_status.head()
transaction_status.plot(kind = "bar")

# using groupby
currency_by_status = sales.groupby("status")["currency"]
currency_by_status.head()



# FILTERING FOR KOREA
Korea = sales.loc["Korea"]
Korea.head(2)
# Lets find out the status of transaction in Korea

failed_transc = Korea[Korea["status"] == "failed"]
successful_transc = Korea[Korea["status"] == "success"]
cancelled_transc = Korea[Korea["status"] == "cancelled"]

# out of this 1,982 customers that experiences failed transaction lets see the numbers of unique customers that there...
failed_transc.customer_id.nunique()

# I would pick each of the customers and check if I can find what really happened...
cust_34d3c5e1= failed_transc[failed_transc["customer_id"] == "34d3c5e1-7e40-40c9-84c3-7d50edfb7eaf"]

# How many transactions did this customer made that ended up failing
cust_34d3c5e1.shape[0]

# What currency was he using to carry out his transactions?
cust_34d3c5e1.currency.unique()

# This customer uses US Dollars($) for transactions...could payment method have associated to the challenge?
# I might still come back to this, to comparw if this customer has any successful transaction...
successful_transc[successful_transc["customer_id"] == "34d3c5e1-7e40-40c9-84c3-7d50edfb7eaf"]

# Unfortunately, this customer never had any "Successful" transation..>
# LEts dig further and check the event time stamp and see if we can discover anything there..
cust_34d3c5e1["event_timestamp"].value_counts()

# What could have happened, all of the above transactions occured within 1 minute, can it be attributed to system error or a kind of fraud?

# LEts try and mop up more evidences as to gain understanding of what happened
cust_34d3c5e1["quantity"].sort_values(ascending = False)

cust_34d3c5e1["order_id"].value_counts()
# the same order_id for all of the transactions

cust_34d3c5e1["item_id"].unique()
#This particular customer tried ordering for 9 different products almostat the same time..

cust_34d3c5e1["item_id"].value_counts()
# Each product was ordered for 22 times...

cust_34d3c5e1["event_id"].nunique()
# We have 22 events each...

cust_34d3c5e1.duplicated().sum() # this customer do not have any duplicate


new_copy = sales.copy()

#### Insights:

#From my discovery in this dataset... I could say that the transactions from customer "cust_34d3c5e1" may not have been carried out by a human because of the consistency of the patterns... the failed transactions may be carried out by a bot or it could be a system error.
#### Recommendation:
#The business and innovation team should look at the case more intensely as I would go on and analyse all other failed transactions to uncover more insights...
#Further more, a compresensive report would be written to highlight the findings of this analysis.

# NUMPY
# Creating arrays from Python lists
# 1D array: A simple sequence of numbers
arr1d = np.array([1, 2, 3, 4, 5])

# 2D array: Think of this as a matrix or table with rows and columns
arr2d = np.array([[1, 2, 3], 
                  [4, 5, 6]])

# 3D array: Like a stack of 2D arrays - useful for images, time series, etc.
arr3d = np.array([[[1, 2], [3, 4]], 
                  [[5, 6], [7, 8]]])

print("1D array:", arr1d)
print("2D array:\n", arr2d)
print("3D array:\n", arr3d)

# CREATING SPECIAL ARRAY*******

# Range arrays - like Python's range() but more powerful
range_arr = np.arange(0, 10, 2)   # Start, stop, step: [0, 2, 4, 6, 8]
print("Range array:", range_arr)

# Linearly spaced arrays - divide a range into equal parts
# From 0 to 1 with exactly 5 points (including endpoints)
linspace_arr = np.linspace(0, 1, 5)  
print("Linspace array:", linspace_arr)

# Logarithmically spaced arrays - useful for scientific data
# From 10^0 to 10^2 (1 to 100) with 5 points
logspace_arr = np.logspace(0, 2, 5)  
print("Logspace array:", logspace_arr)

# ARRAY PROPERTIES AND ATTRIBUTE*********
# Create a sample 3D array for demonstration
# Think of this as 3 layers, each with 4 rows and 5 columns
arr = np.random.randn(3, 4, 5)

# Shape: The dimensions of the array (layers, rows, columns)
print("Shape:", arr.shape)           # Output: (3, 4, 5)

# Size: Total number of elements (3 × 4 × 5 = 60)
print("Size:", arr.size)             

# Ndim: Number of dimensions (3D in this case)
print("Ndim:", arr.ndim)             

# Dtype: Data type of elements
print("Dtype:", arr.dtype)           # Usually float64 for random numbers

# Itemsize: Memory size of each element in bytes
print("Itemsize:", arr.itemsize)     # 8 bytes for float64

# Total memory usage in bytes
print("Memory usage:", arr.nbytes, "bytes")  # size × itemsize
print("Memory usage:", arr.nbytes / 1024, "KB")  # Convert to KB

# BASIC INDEXING*******
# 2D array indexing - row and column access
arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])

# Access specific element: [row, column]
print("Element at row 1, column 2:", arr2d[1, 2])        # 7

# Access entire rows or columns
print("First row:", arr2d[0, :])               # All columns of row 0
print("Second column:", arr2d[:, 1])           # All rows of column 1

# Subarray slicing: [row_start:row_end, col_start:col_end]
print("Subarray (rows 1-2, cols 1-2):\n", arr2d[1:3, 1:3])

# 2D fancy indexing - select specific row/column combinations
arr2d = np.arange(12).reshape(3, 4)  # 3x4 array: [[0,1,2,3], [4,5,6,7], [8,9,10,11]]
print("Original 2D array:\n", arr2d)

# Select elements at (row, col) pairs: (0,1) and (2,3)
rows = np.array([0, 2])
cols = np.array([1, 3])
print("Elements at (0,1) and (2,3):", arr2d[rows, cols])  # [1, 11]

# Select entire rows using fancy indexing
selected_rows = arr2d[[0, 2], :]  # Rows 0 and 2, all columns
print("Selected rows:\n", selected_rows)



# ARRAY RESHAPING AND MANIPULATION****
# Start with a 1D array
arr = np.arange(12)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print("Original 1D array:", arr)

# Reshape to 2D: 3 rows × 4 columns
reshaped_2d = arr.reshape(3, 4)
print("Reshaped to 3x4:\n", reshaped_2d)

# Reshape to 3D: 2 layers × 2 rows × 3 columns  
reshaped_3d = arr.reshape(2, 2, 3)
print("Reshaped to 2x2x3:\n", reshaped_3d)

# Use -1 to let NumPy calculate one dimension automatically
auto_reshape = arr.reshape(4, -1)  # 4 rows, NumPy calculates columns
print("Auto-reshaped to 4x?:\n", auto_reshape)


# TRANSPOSING******
# 2D transposition - flip rows and columns
arr2d = np.array([[1, 2, 3], 
                  [4, 5, 6]])
print("Original shape:", arr2d.shape)      # (2, 3)
print("Original:\n", arr2d)

print("Transposed shape:", arr2d.T.shape)   # (3, 2)
print("Transposed:\n", arr2d.T)

# Alternative transpose methods
print("Transpose method:\n", arr2d.transpose())
# Higher-dimensional transposition
arr3d = np.arange(24).reshape(2, 3, 4)  # 2 layers, 3 rows, 4 columns
print("Original 3D shape:", arr3d.shape)

# Specify new axis order: (axis0, axis1, axis2) → (axis2, axis0, axis1)
transposed_3d = arr3d.transpose(2, 0, 1)
print("Transposed 3D shape:", transposed_3d.shape)  # (4, 2, 3)

# moveaxis is another way to rearrange axes
moved = np.moveaxis(arr3d, 0, -1)  # Move first axis to last position
print("Moveaxis result shape:", moved.shape)


# BASIC ARRAY OPERATION******
# Basic arithmetic operations work element-by-element
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([10, 20, 30, 40])

print("Array 1:", arr1)
print("Array 2:", arr2)

# All operations happen element-wise automatically
print("Addition:", arr1 + arr2)               # [11, 22, 33, 44]
print("Subtraction:", arr2 - arr1)            # [9, 18, 27, 36]
print("Multiplication:", arr1 * arr2)         # [10, 40, 90, 160]
print("Division:", arr2 / arr1)               # [10, 10, 10, 10]
print("Power:", arr1 ** 2)                    # [1, 4, 9, 16]
print("Modulo:", arr2 % 3)

# Common mathematical functions
arr = np.array([1, 4, 9, 16, 25])
print("Original array:", arr)

# Square roots and powers
print("Square root:", np.sqrt(arr))           # [1, 2, 3, 4, 5]
print("Square:", np.square(arr))              # [1, 16, 81, 256, 625]
print("Cube root:", np.cbrt(arr))

# Exponential and logarithmic functions
small_arr = np.array([1, 2, 3])
print("Exponential:", np.exp(small_arr))      # [e^1, e^2, e^3]
print("Natural log:", np.log(arr))            # ln(arr)
print("Log base 10:", np.log10(arr))
print("Log base 2:", np.log2(arr))

# Broadcasting examples - arrays don't need the same shape!
scalar = 5
arr1d = np.array([1, 2, 3, 4])
arr2d = np.array([[10], [20], [30]])  # Column vector

print("Scalar:", scalar)
print("1D array:", arr1d)  
print("2D array (column vector):\n", arr2d)

# Scalar broadcasts to any shape
result1 = scalar + arr1d
print("Scalar + 1D array:", result1)         # [6, 7, 8, 9]

# 2D + 1D broadcasting
result2 = arr2d + arr1d
print("2D + 1D broadcasting:\n", result2)