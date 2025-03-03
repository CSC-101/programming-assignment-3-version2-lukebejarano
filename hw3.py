from data import CountyDemographics




def population_total(counties:list[CountyDemographics])->int:
   total:int = 0
   for county in counties:
       total += county.population["2014 Population"]
   return total


#Task2
def filter_by_state(counties: list[CountyDemographics], state_abbr: str) ->list[CountyDemographics]:
   return [county for county in counties if county.state.upper() == state_abbr.upper()]


#Task3
# Part 3




def population_by_education(counties: list[CountyDemographics], education_key: str) -> float:
  total: float = 0.0
  for county in counties:
      percentage = county.education.get(education_key)
      if percentage is not None:
          pop_2014 = county.population.get("2015 Population", 0)
          total += pop_2014 * (percentage / 100.0)
  return total




def population_by_ethnicity(counties: list[CountyDemographics], ethnicity_key: str) -> float:
  total: float = 0.0
  for county in counties:
      percentage = county.ethnicities.get(ethnicity_key)
      if percentage is not None:
          population_2014 = county.population.get("2014 Population", 0)
          total +=population_2014 * (percentage / 100.0)
  return total




def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
  total: float = 0.0
  for county in counties:
      percentage = county.income.get("Persons Below Poverty Level")
      if percentage is not None:
          population_2014 = county.population.get("2014 Population",0)
          total += population_2014 * (percentage / 100.0)
  return total






# Part 4




def percent_by_education(counties: list[CountyDemographics], education_key: str) -> float:




  total_population = 0
  total_education_population = 0.0
  for county in counties:
      # Get the 2014 population for this county.
      pop_2014 = county.population.get("2014 Population", 0)
      total_population += pop_2014




      # Get the education percentage for the specified key.
      edu_percentage = county.education.get(education_key)
      if edu_percentage is not None:
          total_education_population += pop_2014 * (edu_percentage / 100.0)




  if total_population == 0:
      return 0.0
  return (total_education_population / total_population) * 100.0




# Part 4.1




def percent_by_ethnicity(counties: list[CountyDemographics], ethnicity_key: str) -> float:




  total_population = 0
  total_ethnicity_population = 0.0
  for county in counties:




      pop_2014 = county.population.get("2014 Population", 0)
      total_population += pop_2014




      ethnicity_percentage = county.ethnicities.get(ethnicity_key)
      if ethnicity_percentage is not None:
          total_ethnicity_population += pop_2014 * (ethnicity_percentage / 100.0)




  if total_population == 0:
      return 0.0
  return (total_ethnicity_population / total_population) * 100.0








# Part 4.2
  # list takes in one parameter of list of counties and returns a percentage of the population below the poverty level
def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:




  total_population = 0
  total_poverty_population = 0.0
  # Statement checks every county in list
  for county in counties:
      # Gets population from 2014 from each county and adds it up
      pop_2014 = county.population.get("2014 Population", 0)
      total_population += pop_2014
      # Gets the percentage of population that is below poverty level
      poverty_percentage = county.income.get("Persons Below Poverty Level")
      if poverty_percentage is not None:
          total_poverty_population += pop_2014 * (poverty_percentage / 100.0)




  if total_population == 0:
      return 0.0
  return (total_poverty_population / total_population) * 100.0




# Part 5
def education_greater_than(counties: list[CountyDemographics], education_key: str, threshold: float) -> list[
  CountyDemographics]:




  result = []
  for county in counties:
      value = county.education.get(education_key)
      if value is not None and value > threshold:
          result.append(county)
  return result




# Education less than




def education_less_than(counties: list[CountyDemographics], education_key: str, threshold: float) -> list[
  CountyDemographics]:




  result = []
  for county in counties:
      value = county.education.get(education_key)
      if value is not None and value < threshold:
          result.append(county)
  return result




# Part 5.1
def ethnicity_greater_than(counties: list[CountyDemographics], ethnicity_key: str, threshold: float) -> list[CountyDemographics]:
  result = []
  for county in counties:
      value = county.ethnicities.get(ethnicity_key)
      if value is not None and value > threshold:
          result.append(county)
  return result




# Ethnicity less than
def ethnicity_less_than(counties: list[CountyDemographics], ethnicity_key: str, threshold: float) -> list[CountyDemographics]:
  result = []
  for county in counties:
      value = county.ethnicities.get(ethnicity_key)
      if value is not None and value < threshold:
          result.append(county)
  return result




# Part 5.3
def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold:float) -> list[CountyDemographics]:
  result = []
  for county in counties:
      value = county.income.get("Persons Below Poverty Level")
      if value is not None and value > threshold:
          result.append(county)
  return result




# Poverty level less than




def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
  result = []
  for county in counties:
      value = county.income.get("Persons Below Poverty Level")
      if value is not None and value < threshold:
          result.append(county)
  return result