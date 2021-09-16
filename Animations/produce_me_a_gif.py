import numpy as np
from matplotlib import pyplot as plt
import Special_States as special
import default_plot as dp

lightColor = "#8bb1cc"
darkColor = "#0f4c75"

plt.rcParams["text.usetex"] = False
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Dejavu Serif'
plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams['animation.writer'] = 'ffmpeg'
plt.rcParams['animation.ffmpeg_args'] = ['-loop', '-1']
plt.rcParams['axes.labelsize'] = 12

case = "dirichlet"
L = np.pi
m = 1
a = L/10
l_0 = 80
l_range = 40

fps = 24
speed = 0.05
T = 4*m*L**2/np.pi
real_time = T/4*(1-0.00325)
time = (real_time/speed)

fig = plt.figure(dpi=300, constrained_layout=True)
gs = fig.add_gridspec(nrows=2, ncols=1)

gaussian = special.Bouncing_Gaussian(case, L, m, l_0, l_range, a)

position_plot = dp.Position_Space_Plot(gaussian, fig, gs, [0,0])
position_plot.set_resolution(5000)
position_plot.expectation_value = True

momentum_plot = dp.Discrete_Momentum_Space_Plot(gaussian, fig, gs, [1,0])
momentum_plot.set_n_bound(100)
momentum_plot.axis.set_ylim([0, 0.25])
momentum_plot.set_resolution(1000)
momentum_plot.expectation_value = True

combined_plot = dp.Multi_Plot(position_plot, momentum_plot)
combined_plot.plot(real_time)
position_plot.axis.set_ylim([-0.08979356106230174, 1.885664782314236])
plt.savefig("bouncing_gaussian_dirichlet_at_" + str(round(real_time, 3)) + "s.png")