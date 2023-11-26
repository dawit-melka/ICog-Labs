import matplotlib.pyplot as plt
import numpy as np

def plot_time_elapsed(model_stats):
    model_names = list(model_stats.keys())
    time_elapsed = [model_stats[name]['time elapsed'] for name in model_names]
    
    plt.figure(figsize=(10, 6))
    plt.subplots_adjust(bottom=0.3)
    plt.barh(model_names, time_elapsed)
    plt.xlabel("Time Elapsed (s)")
    plt.ylabel("Model Names")
    plt.title('Time Elapsed Comparison')
    plt.show()
    
def plot_total_error(model_stats):
    model_names = list(model_stats.keys())
    total_error = [model_stats[name]['total error'] for name in model_names]
    
    plt.figure(figsize=(10, 6))
    plt.barh(model_names, total_error, color='maroon')
    plt.xlabel("Total Error")
    plt.ylabel("Model Names")
    plt.title('Total Error Comparison')
    plt.xlim(150, 250)
    plt.show()

def plot_results_comparison(model_stats):
    model_names = list(model_stats.keys())
    first_results = [model_stats[name]['first results'] for name in model_names]
    second_results = [model_stats[name]['second results'] for name in model_names]
    third_results = [model_stats[name]['third results'] for name in model_names]
    total_found = [model_stats[name]['total found'] for name in model_names]

    barWidth = 0.25
    r1 = np.arange(len(model_names))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    r4 = [x + barWidth for x in r3]

    plt.subplots_adjust(bottom=0.3)
    plt.bar(r1, total_found, color='blue', width=barWidth, edgecolor='gray', label='Total Found')
    plt.bar(r2, first_results, color='green', width=barWidth, edgecolor='gray', label='First Results')
    plt.bar(r3, second_results, color='orange', width=barWidth, edgecolor='gray', label='Second Results')
    plt.bar(r4, third_results, color='yellow', width=barWidth, edgecolor='gray', label='Third Results')

    plt.xlabel("Model Names")
    plt.ylabel("Number of Top 3 Results")
    plt.title('Results Comparison')
    plt.xticks([r + barWidth for r in range(len(model_names))], model_names, rotation=45, ha='right')
    plt.legend()

    for i in range(len(model_names)):
        plt.text(r1[i], total_found[i], str(total_found[i]), color='black', ha='center')
        plt.text(r2[i], first_results[i], str(first_results[i]), color='black', ha='center')
        plt.text(r3[i], second_results[i], str(second_results[i]), color='black', ha='center')
        plt.text(r4[i], third_results[i], str(third_results[i]), color='black', ha='center')
    
    plt.show()

# hey codium implement a main function that calls the above 3 ploting functions
def main():
    # Call the plot functions
    model_stats = {'multi-qa-mpnet-base-dot-v1': {'time elapsed': 32.67977476119995, 'total error': 161, 'total found': 13, 'first results': 4, 'second results': 1, 'third results': 2}, 'all-mpnet-base-v2': {'time elapsed': 34.893908977508545, 'total error': 225, 'total found': 7, 'first results': 3, 'second results': 1, 'third results': 0}, 'multi-qa-distilbert-cos-v1': {'time elapsed': 17.127830743789673, 'total error': 210, 'total found': 9, 'first results': 2, 'second results': 1, 'third results': 1}, 'all-distilroberta-v1': {'time elapsed': 26.687182188034058, 'total error': 247, 'total found': 6, 'first results': 0, 'second results': 2, 'third results': 1}, 'all-MiniLM-L12-v2': {'time elapsed': 11.73127007484436, 'total error': 226, 'total found': 8, 'first results': 1, 'second results': 1, 'third results': 0}, 'multi-qa-MiniLM-L6-cos-v1': {'time elapsed': 6.0773162841796875, 'total error': 221, 'total found': 8, 'first results': 3, 'second results': 0, 'third results': 0}, 'msmarco-distilbert-dot-v5': {'time elapsed': 15.681886434555054, 'total error': 207, 'total found': 9, 'first results': 1, 'second results': 1, 'third results': 3}}
    plot_time_elapsed(model_stats)
    plot_results_comparison(model_stats)
    plot_total_error(model_stats)
if __name__ == '__main__':
    main()
    
