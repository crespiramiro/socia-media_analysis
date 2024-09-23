from scripts import data_visualization, data_cleaning, data_analysis, data_plotting, country_plot, age_hist, age_range, likes_scatter
import matplotlib.pyplot as plt  # Importar para mostrar las gráficas juntas

# Step 1: Visualize raw data
print("Step 1: Visualizing raw data...")
data_visualization.main()

# Step 2: Clean the data
print("Step 2: Cleaning the data...")
data_cleaning.main()

# Step 3: Analyze the data
print("Step 3: Analyzing the data...")
data_analysis.main()

# Step 4: Plot the data
print("Step 4: Plotting the data...")
data_plotting.main()
country_plot.main()
age_hist.main()
age_range.main()
likes_scatter.main()


# Display all figures together at the end
plt.show()  # Mostrar todas las gráficas al final
