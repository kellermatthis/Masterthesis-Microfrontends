import matplotlib.pyplot as plt
import matplotlib as mpl

label_size = 15
mpl.rcParams['xtick.labelsize'] = label_size
mpl.rcParams['ytick.labelsize'] = label_size

f,ax = plt.subplots(1,1, figsize=(10,5)) 
plt.xlabel("Anzahl Libs $\\O\\,272$ KB", fontsize=15)
plt.ylabel("Datenmenge in KB", fontsize=15)
plt.plot([0, 1, 3, 5, 8], [1824, 1914, 2218, 3000, 4100], label="Web Components", marker="v", linewidth=3, markersize=10)
plt.plot([0, 1, 3, 5, 8], [2609, 2611, 2613, 2613, 2616], label="Module Federation \nWeb Components", marker="*", linewidth=3, markersize=10)

plt.xlim(-0.2, 8.2)
plt.xticks([0,1,2,3,4,5,6,7,8])
#plt.title("Titel")
plt.legend(fontsize=14)
plt.savefig("MFWCvsMF_Datasize.pdf")
plt.show()
