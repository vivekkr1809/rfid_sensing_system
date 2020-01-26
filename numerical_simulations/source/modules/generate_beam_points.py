import numpy as np


class GenerateBeamPoints():
  """Generate random points in a beam
  """
  def __init__(self, beam_length, beam_width, beam_height, young_modulus):
    self.beam_l = beam_length
    self.beam_w = beam_width
    self.beam_h = beam_height
    self.E = young_modulus
    self.I = (beam_height**3)*(beam_width)/(12.0)

  def sample_random_points(self, n_points):
    """Generate n points in the beam
    """
    # Fix the random seed
    np.random.seed(42)
    
    # Obtain the original points
    self.n_points = n_points

    self.original_interior_points = np.random.rand(self.n_points, 3)
    self.original_interior_points[:,0] = self.original_interior_points[:,0,]*self.beam_l
    self.original_interior_points[:,1] = self.original_interior_points[:,1,]*self.beam_w
    self.original_interior_points[:,2] = self.original_interior_points[:,2,]*self.beam_h
    return self.original_interior_points
  
  def obtain_deformed_points(self, support_condition, loading_condition, load):
    deformed_points = np.zeros((self.n_points,3))
    if(support_condition=='simply_supported'):
      if(loading_condition=='uniformly_loaded'):
        deformed_points[:,0] = self.original_interior_points[:,0]
        deformed_points[:,1] = self.original_interior_points[:,1]
        for i in range(self.n_points):
          deformed_points[i,2] = (load*self.original_interior_points[i,0]/(24.*self.E*self.I))*(self.beam_l**3 - 2.*self.beam_l*(self.original_interior_points[i,0]**2)+ (self.original_interior_points[i,0]**3))
        return deformed_points




if __name__ == '__main__':
  l = 5.
  w = 3.
  h = 2.
  E = 1e6
  
  beam_points = GenerateBeamPoints(l,w,h,E)
  original_points = beam_points.sample_random_points(10)
  deformed_points = beam_points.obtain_deformed_points('simply_supported', 'uniformly_loaded', 10.)

  