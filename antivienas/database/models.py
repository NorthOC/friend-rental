from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

#TODO: ADD PAYMENT HISTORY MODEL
#TODO: ADD REVIEW MODEL
#TODO: ADD ORDER MODEL
#TODO: ADD WITHDRAWAL REQUEST MODEL

class CityOfService(models.TextChoices):
    """ List of Lithuanian cities """
    VILNIUS = "Vilnius"
    KAUNAS = "Kaunas"
    KLAIPEDA = "Klaipėda"
    SIAULIAI = "Šiauliai"
    PANEVEZYS = "Panevėžys"
    AKMENE = "Akmenė"
    ALYTUS = "Alytus"
    ANYKSCIAI = "Anykščiai"
    BIRSTONAS = "Birštonas"
    BIRZAI = "Biržai"
    DRUSKININKAI = "Druskininkai"
    ELEKTRENAI = "Elektrėnai"
    GARGZDAI = "Gargždai"
    IGNALINA = "Ignalina"
    JONAVA = "Jonava"
    JONISKIS = "Joniškis"
    JURBARKAS = "Jurbarkas"
    KAISIADORYS = "Kaišiadorys"
    KALVARIJA = "Kalvarija"
    KAZLU_RUDA = "Kazlų Rūda"
    KEDAINIAI = "Kėdainiai"
    KELME = "Kelmė"
    KREKENAVA = "Krekenava"
    KRETINGA = "Kretinga"
    KUPISKIS = "Kupiškis"
    KURSENAI = "Kuršėnai"
    LAZDIJAI = "Lazdijai"
    LENTVARIS = "Lentvaris"
    MARIJAMPOLE = "Marijampolė"
    MAZEIKIAI = "Mažeikiai"
    MOLETAI = "Molėtai"
    NAUJOJI_AKMENE = "Naujoji Akmenė"
    NEMENCINE = "Nemenčinė"
    NERINGA = "Neringa"
    PABRADE = "Pabradė"
    PAGEGIAI = "Pagėgiai"
    PAKRUOJIS = "Pakruojis"
    PALANGA = "Palanga"
    PASVALYS = "Pasvalys"
    PLUNGE = "Plungė"
    PRIENAI = "Prienai"
    RADVILISKIS = "Radviliškis"
    RASEINIAI = "Raseiniai"
    RIETAVAS = "Rietavas"
    ROKISKIS = "Rokiškis"
    SAKIAI = "Šakiai"
    SALCININKAI = "Šalčininkai"
    SILALE = "Šilalė"
    SILUTE = "Šilutė"
    SIRVINTOS = "Širvintos"
    SKUODAS = "Skuodas"
    SVENCIONYS = "Švenčionys"
    TAURAGE = "Tauragė"
    TELSIAI = "Telšiai"
    TRAKAI = "Trakai"
    UKMERGE = "Ukmergė"
    UTENA = "Utena"
    VARENA = "Varėna"
    VIEVIS = "Vievis"
    VILKAVISKIS = "Vilkaviškis"
    VISAGINAS = "Visaginas"
    ZARASAI = "Zarasai"
    NUOTOLINIU = "Nuotoliniu"

class Genders(models.TextChoices):
    VYR = "vyr"
    MOT = "mot"

def user_img_upload_path(instance, filename):
    return f"user_uploads/user_{instance.pk}/{filename}"

class User(AbstractUser):
    """
    User model
    ________________
    +email
    +password
    +is_activated - used for email activation
    +is_id_verified - use for id verification
    +profile_type - determines if user or friend

    +wallet - virtual wallet

    +first_name
    +last_name
    +birthday
    +city - choice where service is provided (remote opt included)
    +education_level - vidurinis, auštasis, aukštesnysis, kitas
    +job
    +description
    +personality_type - 16 types
    +sex - vyr, mot
    +height_cm

    +img_one     --
    +img_two      |______ images
    +img_three   --
    +interest_one    --
    +interest_two     |_____ interests
    +interest_three   |
    +interest_four   --
    +interest_color_one      --
    +interest_color_two       |_____ interest box bg color
    +interest_color_three     |
    +interest_color_four     --
    """

    class ProfileTypes(models.TextChoices):
        # users have a different profile type from friends
        USER = "User"
        FRIEND = "Friend"
    
    class EducationLevels(models.TextChoices):
        VIDURINIS = "Vidurinis"
        AUKSTESNYSIS = "Aukštesnysis"
        AUKSTASIS = "Aukštasis"
    
    class PersonalityTypes(models.TextChoices):
        INTRAVERT = "Intravert"
        EKSTRAVERT = "Ekstravert"

    class InterestColorHexes(models.TextChoices):
        GRAY = "#D9D9D9"
        RED = "#F6C4C4"
        BLUE = "#B2D8EE"
        GREEN = "#B8F2C1"
        PURPLE = "#F1B8F2"

    # for login (using email)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    is_activated = models.BooleanField(default=False)
    is_id_verified = models.BooleanField(default=False)

    profile_type = models.CharField(max_length=6, 
                                    choices=ProfileTypes, 
                                    default=ProfileTypes.USER)
    wallet = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    birthday = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=15,
                            choices=CityOfService,
                            null=True,
                            blank=True)
    job = models.CharField(max_length=40, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    personality_type = models.CharField(max_length=10,
                                        choices=PersonalityTypes,
                                        null=True,
                                        blank=True)
    sex = models.CharField(max_length=3, choices=Genders, blank=True, null=True)
    height_cm = models.PositiveIntegerField(blank=True, 
                                            null=True, 
                                            validators=[MinValueValidator(0), MaxValueValidator(300)])

    img_one = models.ImageField(upload_to=user_img_upload_path, blank=True, null=True)
    img_two = models.ImageField(upload_to=user_img_upload_path, blank=True, null=True)
    img_three = models.ImageField(upload_to=user_img_upload_path, blank=True, null=True)

    interest_one =      models.CharField(max_length=25, blank=True, null=True)
    interest_two =      models.CharField(max_length=25, blank=True, null=True)
    interest_three =    models.CharField(max_length=25, blank=True, null=True)
    interest_four =     models.CharField(max_length=25, blank=True, null=True)

    interest_color_one = models.CharField(max_length=7, choices=InterestColorHexes, default=InterestColorHexes.GRAY)
    interest_color_two = models.CharField(max_length=7, choices=InterestColorHexes, default=InterestColorHexes.GRAY)
    interest_color_three = models.CharField(max_length=7, choices=InterestColorHexes, default=InterestColorHexes.GRAY)
    interest_color_four = models.CharField(max_length=7, choices=InterestColorHexes, default=InterestColorHexes.GRAY)

