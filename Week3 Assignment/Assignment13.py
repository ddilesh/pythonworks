import numpy as np


data = np.random.randint(5, 51, size=(5, 50))
print("Execution Times (5x50 Matrix):\n", data, "\n")


avg_per_cycle = np.mean(data, axis=1)
print("Average execution time per cycle:", avg_per_cycle)


max_time = np.max(data)
max_location = np.unravel_index(np.argmax(data), data.shape)  # gives (row, col)
print("Maximum execution time:", max_time, "at cycle", max_location[0]+1, "test", max_location[1]+1)


std_per_cycle = np.std(data, axis=1)
print("Standard deviation per cycle:", std_per_cycle, "\n")


print("First 10 tests from Cycle 1:", data[0, :10])
print("Last 5 tests from Cycle 5:", data[4, -5:])
print("Every alternate test from Cycle 3:", data[2, ::2], "\n")


print("Cycle 1 + Cycle 2:\n", data[0] + data[1])
print("Cycle 1 - Cycle 2:\n", data[0] - data[1])
print("Cycle 4 * Cycle 5:\n", data[3] * data[4])
print("Cycle 4 / Cycle 5:\n", data[3] / data[4], "\n")


print("Squared values:\n", np.power(data, 2))
print("Cubed values:\n", np.power(data, 3))
print("Square root:\n", np.sqrt(data))
print("Log-transformed:\n", np.log(data + 1), "\n")


shallow = data.view()
shallow[0, :5] = 99
print("After modifying shallow copy, original data[0, :5]:", data[0, :5])


deep = data.copy()
deep[1, :5] = 77
print("After modifying deep copy, original data[1, :5]:", data[1, :5], "\n")


cycle2_gt30 = data[1, data[1] > 30]
print("Cycle 2 tests > 30:", cycle2_gt30)


consistently_gt25 = np.all(data > 25, axis=0)
print("Tests consistently > 25 across cycles:", data[:, consistently_gt25])


thresholded_data = np.where(data < 10, 10, data)
print("Data after thresholding (<10 replaced with 10):\n", thresholded_data)
