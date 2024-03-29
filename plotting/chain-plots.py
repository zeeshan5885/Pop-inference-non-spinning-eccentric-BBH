import numpy as np
import matplotlib.pyplot as plt
import h5py

data1 = h5py.File('myout.hdf5','r')
data2 = h5py.File('myout_org.hdf5','r')
data_3D1 = np.array(data1['pos'])
data_3D2 = np.array(data2['pos'])
fig, axes = plt.subplots(5, figsize=(12, 12), sharex=True)
samples = data_3D1
labels = ["$log_{10}(\mathcal{R})$",r"$\alpha$", "$m_{min}$","$m_{max}$","$\sigma_\epsilon$"]
for i in range(5):
 ax = axes[i]
 ax.plot(samples[:, :, i],'-', alpha=0.3)
 ax.set_xlim(0, len(samples))
 ax.set_ylabel(labels[i])
 plt.savefig("chain.png")
axes[-1].set_xlabel("step number");
plt.figure()
plt.plot(samples[:,:,0], '-', color='k')
plt.xlabel("step number")
plt.ylabel("$log_{10}(\mathcal{R})$")
plt.savefig('rate.png')
plt.figure()
plt.plot(samples[:,:,1], '-', color='k')
plt.xlabel("step number")
plt.ylabel(r"$\alpha$")
plt.savefig('alpha.png')
plt.figure()
plt.plot(samples[:,:,2], '-', color='k')
plt.xlabel("step number")
plt.ylabel(r"$m_{min}$")
plt.savefig('min.png')
plt.figure()
plt.plot(samples[:,:,3], '-', color='k')
plt.xlabel("step number")
plt.ylabel(r"$m_{max}$")
plt.savefig('max.png')
plt.figure()
plt.plot(samples[:,:,4], '-', color='k')
plt.xlabel("step number")
plt.ylabel("$\sigma_\epsilon$")
plt.savefig('sigecc.png')

# The following chain plots are for the NEBBHs
samples1 = data_3D2
labels1 = ["$log_{10}(\mathcal{R})$",r"$\alpha$", "$m_{min}$","$m_{max}$"]
for i in range(4):
 ax = axes[i]
 ax.plot(samples1[:, :, i],'-', alpha=0.3)
 ax.set_xlim(0, len(samples1))
 ax.set_ylabel(labels1[i])
 plt.savefig("chain_org.png")
axes[-1].set_xlabel("step number")
plt.figure()
plt.plot(samples1[:,:,0], '-', color='k')
plt.xlabel("step number")
plt.ylabel("$log_{10}(\mathcal{R})$")
plt.savefig('rate_org.png')
plt.figure()
plt.plot(samples1[:,:,1], '-', color='k')
plt.xlabel("step number")
plt.ylabel(r"$\alpha$")
plt.savefig('alpha_org.png')
plt.figure()
plt.plot(samples1[:,:,2], '-', color='k')
plt.xlabel("step number")
plt.ylabel(r"$m_{min}$")
plt.savefig('min_org.png')
plt.figure()
plt.plot(samples1[:,:,3], '-', color='k')
plt.xlabel("step number")
plt.ylabel(r"$m_{max}$")
plt.savefig('max_org.png')
plt.figure()
