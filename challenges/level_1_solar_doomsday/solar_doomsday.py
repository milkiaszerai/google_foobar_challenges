import math

def solution(area=0):
  """
    Creates list of square panels from given area

    Args:
        area (sq. yards): total area of solar panels in range [1, 1000000]. Default = 0 

    Returns:
        panels (list): list of the areas of the largest squares you could make out of those panels. 
  """

  # Initialize empty list to store the square panels
  panels = []
  area_ = area   # area_ = area remaining after each iteration
  
  while True:
    panel = math.sqrt(area_)
    panel = (int(panel))**2
    panels.append(panel)
    area_ = area - sum(panels) 
    if area_ == 0:
      break
  return panels 

if __name__ == "__main__":
    solution()

