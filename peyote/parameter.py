from __future__ import division, print_function
import numpy as np
import peyote


class Parameter:

    def __init__(self, name, prior=None, value=None, latex_label=None, is_fixed=False):
        self.name = name

        self.prior = prior
        self.value = value
        self.latex_label = latex_label
        self.is_fixed = is_fixed

    @property
    def prior(self):
        return self.__prior

    @property
    def value(self):
        return self.__value

    @property
    def latex_label(self):
        return self.__latex_label

    @property
    def is_fixed(self):
        return self.__is_fixed

    @prior.setter
    def prior(self, prior=None):
        if prior is None:
            self.set_default_prior()
        else:
            self.__prior = prior

    @value.setter
    def value(self, value=None):
        if value is None:
            self.set_default_values()
        else:
            self.__value = value

    @latex_label.setter
    def latex_label(self, latex_label=None):
        if latex_label is None:
            self.set_default_latex_label()
        else:
            self.__latex_label = latex_label

    @is_fixed.setter
    def is_fixed(self, is_fixed):
        if is_fixed:
            self.__is_fixed = True
        else:
            self.__is_fixed = False

    def fix(self, value=None):
        """
        Specify parameter as fixed, this will not be sampled.
        """
        self.is_fixed = True
        if value is not None:
            self.value = value
        elif self.value == np.nan:
            raise ValueError("You can't fix the value to be np.nan. You need to assign it a legal value")
        self.prior = None

    def set_default_prior(self):

        if self.name == 'mass_1':
            self.__prior = peyote.prior.PowerLaw(alpha=0, bounds=(5, 100))
        elif self.name == 'mass_2':
            self.__prior = peyote.prior.PowerLaw(alpha=0, bounds=(5, 100))
        elif self.name == 'mchirp':
            self.__prior = peyote.prior.PowerLaw(alpha=0, bounds=(5, 100))
        elif self.name == 'q':
            self.__prior = peyote.prior.PowerLaw(alpha=0, bounds=(0, 1))
        elif self.name == 'a1':
            self.__prior = peyote.prior.PowerLaw(alpha=0, bounds=(0, 1))
        elif self.name == 'a2':
            self.__prior = peyote.prior.PowerLaw(alpha=0, bounds=(0, 1))
        elif self.name == 'tilt1':
            self.__prior = peyote.prior.Sine()
        elif self.name == 'tilt2':
            self.__prior = peyote.prior.Sine()
        elif self.name == 'phi1':
            self.__prior = peyote.prior.PowerLaw(alpha=0, bounds=(0, 2 * np.pi))
        elif self.name == 'phi2':
            self.__prior = peyote.prior.PowerLaw(alpha=0, bounds=(0, 2 * np.pi))
        elif self.name == 'luminosity_distance':
            self.__prior = peyote.prior.PowerLaw(alpha=2, bounds=(1e2, 5e3))
        elif self.name == 'dec':
            self.__prior = peyote.prior.Cosine()
        elif self.name == 'ra':
            self.__prior = peyote.prior.PowerLaw(alpha=0, bounds=(0, 2 * np.pi))
        elif self.name == 'iota':
            self.__prior = peyote.prior.Sine()
        elif self.name == 'psi':
            self.__prior = peyote.prior.PowerLaw(alpha=0, bounds=(0, 2 * np.pi))
        elif self.name == 'phase':
            self.__prior = peyote.prior.PowerLaw(alpha=0, bounds=(0, 2 * np.pi))
        else:
            self.__prior = None

    def set_default_values(self):
        # spins
        if self.name == 'a1':
            self.__value = 0
        elif self.name == 'a2':
            self.__value = 0
        elif self.name == 'tilt1':
            self.__value = 0
        elif self.name == 'tilt2':
            self.__value = 0
        elif self.name == 'phi1':
            self.__value = 0
        elif self.name == 'phi2':
            self.__value = 0
        else:
            self.__value = np.nan

    def set_default_latex_label(self):
        if self.name == 'mass_1':
            self.__latex_label = '$m_1$'
        elif self.name == 'mass_2':
            self.__latex_label = '$m_2$'
        elif self.name == 'mchirp':
            self.__latex_label = '$\mathcal{M}$'
        elif self.name == 'q':
            self.__latex_label = 'q'
        elif self.name == 'a1':
            self.__latex_label = 'a_1'
        elif self.name == 'a2':
            self.__latex_label = 'a_2'
        elif self.name == 'tilt1':
            self.__latex_label = 'tilt_1'
        elif self.name == 'tilt2':
            self.__latex_label = 'tilt_2'
        elif self.name == 'phi1':
            self.__latex_label = '\phi_1'
        elif self.name == 'phi2':
            self.__latex_label = '\phi_2'
        elif self.name == 'luminosity_distance':
            self.__latex_label = 'd'
        elif self.name == 'dec':
            self.__latex_label = '\mathrm{DEC}'
        elif self.name == 'ra':
            self.__latex_label = '\mathrm{RA}'
        elif self.name == 'iota':
            self.__latex_label = '\iota'
        elif self.name == 'psi':
            self.__latex_label = '\psi'
        elif self.name == 'phase':
            self.__latex_label = '\phi'
        elif self.name == 'tc':
            self.__latex_label = 't_c'
        else:
            self.__latex_label = self.name
