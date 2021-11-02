constant_definitions = []

class constantDefiner:
    def __init__(self, identifiers, value):
        self.identifiers = identifiers
        self.value = value

def addConstant(identifiers, value):
    new_constant = constantDefiner(identifiers, value)
    constant_definitions.append(new_constant)

# Mathematical constants
addConstant(["$pi"], 3.14159265358979323846)
addConstant(["$e"], 2.718281828459045)
addConstant(["$phi", "$gr"], 1.61803398874989484820)
addConstant(["$feigenbaum"], 4.669201609102990671853203820466)

# Universal constants
addConstant(["$c"], 299792458)
addConstant(["$G"], 6.67384e-11)
addConstant(["$g"], 9.80665)
addConstant(["$h"], 6.62606957e-34)
addConstant(["$rh", "$hbar"], 1.054571726e-34)
addConstant(["$R"], 8.3144621)

# Electromagnetic constants
addConstant(["$mu_0", "$mu0"], 1.256637061e-6)
addConstant(["$epsilon_0", "$epsilon0"], 8.854187817e-12)
addConstant(["$Z", "$Z_0", "$Z0"], 376.730313461)
addConstant(["$k"], 8.987551787e9)
addConstant(["$e"], 1.602176565e-19)
addConstant(["$mu_b"], 9.27400968e-24)
addConstant(["$mu_n"], 5.05078353e-27)
addConstant(["$von_k"], 25812.8074434)

# Atomic and nuclear constants
addConstant(["$a_0"], 5.2917721092e-11)
addConstant(["$e_m"], 9.10938291e-31)
addConstant(["$p_m"], 1.672621777e-27)
addConstant(["$n_m"], 1.674927211e-27)
addConstant(["$fine_str"], 7.2973525698e-3)
addConstant(["$hartree"], 4.35974434e-18)
addConstant(["$ryd", "$rydberg"], 10973731.568539)

# Physio - chemical constants
addConstant(["$amu", "$u"], 1.660538921e-27)
addConstant(["$avo", "$avogadro", "$Na", "$N_a"], 6.02214129e23)
addConstant(["$boltzmann", "$kb", "$k_b"], 1.3806488e-23)
addConstant(["$faraday", "$F"], 96485.3365)
addConstant(["$c1"], 3.74177153e-16)
addConstant(["$c2"], 1.4387770e-2)
addConstant(["$stefan", "$sb", "$sigma"], 5.670373e-8)
addConstant(["$wien", "$b"], 2.8977721e-3)