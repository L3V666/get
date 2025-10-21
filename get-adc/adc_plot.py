from matplotlib import pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage)
    plt.show()

def plot_sampling_period_hist(time):
    sampling_period = []
    for i in range(1, len(time)):
        sampling_period.append(time[i] - time[i - 1])
    print(time)
    print(sampling_period)
    plt.figure(figsize=(10, 6))
    plt.hist(sampling_period)
    plt.show()