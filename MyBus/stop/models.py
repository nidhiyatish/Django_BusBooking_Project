from django.db import models

# stop app
# Create your models here.




class Stop(models.Model):
    CITY_CHOICES = [
    ("ahmedabad", "Ahmedabad"),
    ("aizawl", "Aizawl"),
    ("ajmer", "Ajmer"),
    ("aligarh", "Aligarh"),
    ("allahabad", "Prayagraj"),
    ("amritsar", "Amritsar"),
    ("bengaluru", "Bengaluru"),
    ("bhavnagar", "Bhavnagar"),
    ("bhilai", "Bhilai"),
    ("bhopal", "Bhopal"),
    ("bhubaneswar", "Bhubaneswar"),
    ("bikaner", "Bikaner"),
    ("chandigarh", "Chandigarh"),
    ("chennai", "Chennai"),
    ("coimbatore", "Coimbatore"),
    ("cuttack", "Cuttack"),
    ("dehradun", "Dehradun"),
    ("delhi", "Delhi"),
    ("dhanbad", "Dhanbad"),
    ("dharamshala", "Dharamshala"),
    ("dibrugarh", "Dibrugarh"),
    ("faridabad", "Faridabad"),
    ("ghaziabad", "Ghaziabad"),
    ("goa", "Goa"),
    ("gorakhpur", "Gorakhpur"),
    ("gurugram", "Gurugram"),
    ("guwahati", "Guwahati"),
    ("gwalior", "Gwalior"),
    ("hyderabad", "Hyderabad"),
    ("imphal", "Imphal"),
    ("indore", "Indore"),
    ("itarsi", "Itarsi"),
    ("jaipur", "Jaipur"),
    ("jalandhar", "Jalandhar"),
    ("jammu", "Jammu"),
    ("jamnagar", "Jamnagar"),
    ("jamshedpur", "Jamshedpur"),
    ("jodhpur", "Jodhpur"),
    ("kanpur", "Kanpur"),
    ("karnal", "Karnal"),
    ("kochi", "Kochi"),
    ("kohima", "Kohima"),
    ("kolkata", "Kolkata"),
    ("kozhikode", "Kozhikode"),
    ("lucknow", "Lucknow"),
    ("ludhiana", "Ludhiana"),
    ("madurai", "Madurai"),
    ("mangalore", "Mangalore"),
    ("meerut", "Meerut"),
    ("mumbai", "Mumbai"),
    ("mysuru", "Mysuru"),
    ("nagpur", "Nagpur"),
    ("nashik", "Nashik"),
    ("noida", "Noida"),
    ("panipat", "Panipat"),
    ("patna", "Patna"),
    ("pondicherry", "Puducherry"),
    ("prayagraj", "Prayagraj"),
    ("pune", "Pune"),
    ("raipur", "Raipur"),
    ("rajkot", "Rajkot"),
    ("ranchi", "Ranchi"),
    ("rohtak", "Rohtak"),
    ("shimla", "Shimla"),
    ("siliguri", "Siliguri"),
    ("srinagar", "Srinagar"),
    ("surat", "Surat"),
    ("thane", "Thane"),
    ("thiruvananthapuram", "Thiruvananthapuram"),
    ("thrissur", "Thrissur"),
    ("tiruchirappalli", "Tiruchirappalli"),
    ("udaipur", "Udaipur"),
    ("ujjain", "Ujjain"),
    ("varanasi", "Varanasi"),
    ("vijayawada", "Vijayawada"),
    ("visakhapatnam", "Visakhapatnam"),
    ("warangal", "Warangal"),]
    name = models.CharField(max_length=100)   
    city = models.CharField(max_length=50, choices= CITY_CHOICES)
    washroom_available = models.BooleanField(default=False)
    image = models.ImageField(upload_to="stop/images/")
    added_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Stop :  {self.name.capitalize()} | City : {self.city.capitalize()}"

    
    