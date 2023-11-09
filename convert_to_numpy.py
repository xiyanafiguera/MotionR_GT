import scipy.io

# Load the original MAT file
path = "Coman/coman_02_05 punch strike.mat"
data = scipy.io.loadmat(path)

# Access q_traj and q_traj_cf
q_traj = data["q_traj"]
q_traj_cf = data["q_traj_cf"]

print(type(q_traj))
print(len(q_traj[0]))
print(q_traj[0])
