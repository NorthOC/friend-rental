from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

#TODO: ADD USER_REPORT MODEL

class CityOfService(models.TextChoices):
    """ List of Lithuanian cities """
    VILNIUS =           "Vilnius"
    KAUNAS =            "Kaunas"
    KLAIPEDA =          "Klaipėda"
    SIAULIAI =          "Šiauliai"
    PANEVEZYS =         "Panevėžys"
    AKMENE =            "Akmenė"
    ALYTUS =            "Alytus"
    ANYKSCIAI =         "Anykščiai"
    BIRSTONAS =         "Birštonas"
    BIRZAI =            "Biržai"
    DRUSKININKAI =      "Druskininkai"
    ELEKTRENAI =        "Elektrėnai"
    GARGZDAI =          "Gargždai"
    IGNALINA =          "Ignalina"
    JONAVA =            "Jonava"
    JONISKIS =          "Joniškis"
    JURBARKAS =         "Jurbarkas"
    KAISIADORYS =       "Kaišiadorys"
    KALVARIJA =         "Kalvarija"
    KAZLU_RUDA =        "Kazlų Rūda"
    KEDAINIAI =         "Kėdainiai"
    KELME =             "Kelmė"
    KREKENAVA =         "Krekenava"
    KRETINGA =          "Kretinga"
    KUPISKIS =          "Kupiškis"
    KURSENAI =          "Kuršėnai"
    LAZDIJAI =          "Lazdijai"
    LENTVARIS =         "Lentvaris"
    MARIJAMPOLE =       "Marijampolė"
    MAZEIKIAI =         "Mažeikiai"
    MOLETAI =           "Molėtai"
    NAUJOJI_AKMENE =    "Naujoji Akmenė"
    NEMENCINE =         "Nemenčinė"
    NERINGA =           "Neringa"
    PABRADE =           "Pabradė"
    PAGEGIAI =          "Pagėgiai"
    PAKRUOJIS =         "Pakruojis"
    PALANGA =           "Palanga"
    PASVALYS =          "Pasvalys"
    PLUNGE =            "Plungė"
    PRIENAI =           "Prienai"
    RADVILISKIS =       "Radviliškis"
    RASEINIAI =         "Raseiniai"
    RIETAVAS =          "Rietavas"
    ROKISKIS =          "Rokiškis"
    SAKIAI =            "Šakiai"
    SALCININKAI =       "Šalčininkai"
    SILALE =            "Šilalė"
    SILUTE =            "Šilutė"
    SIRVINTOS =         "Širvintos"
    SKUODAS =           "Skuodas"
    SVENCIONYS =        "Švenčionys"
    TAURAGE =           "Tauragė"
    TELSIAI =           "Telšiai"
    TRAKAI =            "Trakai"
    UKMERGE =           "Ukmergė"
    UTENA =             "Utena"
    VARENA =            "Varėna"
    VIEVIS =            "Vievis"
    VILKAVISKIS =       "Vilkaviškis"
    VISAGINAS =         "Visaginas"
    ZARASAI =           "Zarasai"
    NUOTOLINIU =        "Nuotoliniu"

class Genders(models.TextChoices):
    VYR = "vyr"
    MOT = "mot"

def user_img_upload_path(instance, filename):
    return f"user_uploads/user_{instance.pk}/{filename}"

class User(AbstractUser):
    """
    Defines the user
    ________________
    is_activated - used for email activation
    is_id_verified - use for id verification
    profile_type - determines if user or friend
    wallet - virtual wallet
    city - choice where service is provided (remote opt included)
    education_level - vidurinis, auštasis, aukštesnysis, kitas
    description - markdown style?
    personality_type - intravert,ekstravert
    settings - friend profiles get settings
    img_one     --
    img_two      |______ images
    img_three   --
    interest_one    --
    interest_two     |_____ interests
    interest_three   |
    interest_four   --
    interest_color_one      --
    interest_color_two       |_____ interest box bg color
    interest_color_three     |
    interest_color_four     --
    """

    class ProfileTypes(models.TextChoices):
        # users have a different profile type from friends
        USER =      "User"
        FRIEND =    "Friend"
    
    class EducationLevels(models.TextChoices):
        VIDURINIS =     "Vidurinis"
        AUKSTESNYSIS =  "Aukštesnysis"
        AUKSTASIS =     "Aukštasis"
    
    class PersonalityTypes(models.TextChoices):
        INTRAVERT =     "Intravert"
        EKSTRAVERT =    "Ekstravert"

    class InterestColorHexes(models.TextChoices):
        GRAY =      "#D9D9D9", "Gray"
        RED =       "#F6C4C4", "Red"
        BLUE =      "#B2D8EE", "Blue"
        GREEN =     "#B8F2C1", "Green"
        PURPLE =    "#F1B8F2", "Purple"

    email =         models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    is_activated = models.BooleanField(default=False)
    is_id_verified = models.BooleanField(default=False)

    profile_type =      models.CharField(max_length=6, choices=ProfileTypes, default=ProfileTypes.USER)
    wallet =            models.DecimalField(max_digits=6, decimal_places=2, default=0)
    birthday =          models.DateField(null=True, blank=True)
    city =              models.CharField(max_length=15,choices=CityOfService,null=True,blank=True)
    job =               models.CharField(max_length=40, null=True, blank=True)
    description =       models.TextField(max_length=5000, null=True, blank=True)
    personality_type =  models.CharField(max_length=10, choices=PersonalityTypes, null=True, blank=True)
    sex =               models.CharField(max_length=3, choices=Genders, blank=True, null=True)
    height_cm =         models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(300)])

    img_one =           models.ImageField(upload_to=user_img_upload_path, blank=True, null=True)
    img_two =           models.ImageField(upload_to=user_img_upload_path, blank=True, null=True)
    img_three =         models.ImageField(upload_to=user_img_upload_path, blank=True, null=True)

    interest_one =      models.CharField(max_length=50, blank=True, null=True)
    interest_two =      models.CharField(max_length=50, blank=True, null=True)
    interest_three =    models.CharField(max_length=50, blank=True, null=True)
    interest_four =     models.CharField(max_length=50, blank=True, null=True)

    interest_color_one =    models.CharField(max_length=7, choices=InterestColorHexes, default=InterestColorHexes.GRAY)
    interest_color_two =    models.CharField(max_length=7, choices=InterestColorHexes, default=InterestColorHexes.GRAY)
    interest_color_three =  models.CharField(max_length=7, choices=InterestColorHexes, default=InterestColorHexes.GRAY)
    interest_color_four =   models.CharField(max_length=7, choices=InterestColorHexes, default=InterestColorHexes.GRAY)

    account_number =            models.CharField(max_length=20, blank=True, null=True)
    account_holder_details =    models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.pk)

class FriendSetting(models.Model):
    """
    When Users become friends, they get special settings
    _________________________________
    is_public - defines if the listing is public
    public_from - last time profile became public
    level - Complete orders increase expertise
    """

    friend =            models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    price_per_hour =    models.PositiveIntegerField(default=0)
    is_public =         models.BooleanField(default=False)

    class LvlOfExperience(models.IntegerChoices):
        NEWBIE      = 1, "Newbie"       # starting lvl
        EXPERIENCED = 2, "Experienced"  # after completing 2 orders
        VETERAN     = 3, "Veteran"      # after completing 10 orders
        EXPERT      = 4, "Expert"       # reserved for psychology majors
    
    level =             models.SmallIntegerField(choices=LvlOfExperience, default=LvlOfExperience.NEWBIE)
    created =           models.DateTimeField(auto_now_add=True)
    public_from =       models.DateTimeField(null=True, blank=True)


class Order(models.Model):
    """
    Defines the order for meeting
    _____________________
    meeting_time - select a date for the meeting
    no_of_hours - number of hours the meeting will take place
    comment - user describes what they are going to do together
    total_price - no_of_hours * friend.settings.price_per_hour
    fee - a % of how greedy I want to be (also transaction fees)
    """
    class OrderStatuses(models.IntegerChoices):
        INITIATED   = 1, 'Initiated'     # when user inits order
        CONFIRMED   = 2, 'Confirmed'     # when friend confirms order
        PAID        = 3, 'Paid'          # when user completes payment
        COMPLETE    = 4, "Complete"      # after the friend receives payment
        CANCELLED   = 5, 'Cancelled'     # if friend doesn't confirm
        ABANDONED   = 6, "Abandoned"     # if user does not complete payment
        DISPUTED    = 7, "Disputed"      # if user disputes order

    user =          models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="user")
    friend =        models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="friend")
    meeting_time =  models.DateTimeField()
    no_of_hours =   models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(24)])
    meeting_place = models.CharField(max_length=300)
    comment =       models.TextField(max_length=1500)
    total_price =   models.DecimalField(max_digits=6, decimal_places=2)
    fee =           models.DecimalField(max_digits=6, decimal_places=2)
    profit =        models.DecimalField(max_digits=6, decimal_places=2)

    order_status =          models.SmallIntegerField(choices=OrderStatuses, default=OrderStatuses.INITIATED)
    order_message_user =    models.CharField(max_length=300)
    order_message_friend =  models.CharField(max_length=300)
    created =               models.DateTimeField(auto_now_add=True)

class UserReview(models.Model):
    """
    Users can review friends if order was complete.
    ________________________
    self-explanatory
    """
    order =         models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    user =          models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="reviewer_user")
    friend =        models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="reviewed_friend")
    rating =        models.PositiveSmallIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(10)])
    comment =       models.TextField(max_length=1000, null=True, blank=True)
    post_as_anon =  models.BooleanField(default=False)
    created =       models.DateTimeField(auto_now_add=True)
    modified =      models.DateTimeField(auto_now=True)

class FriendReview(models.Model):
    """
    Friends can review users after order is complete.
    ________________________
    self-explanatory
    """
    order =         models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    friend =        models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="reviewer_friend")
    user =          models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="reviewed_user")
    rating =        models.PositiveSmallIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(10)])
    comment =       models.TextField(max_length=1000, null=True, blank=True)
    post_as_anon =  models.BooleanField(default=False)
    created =       models.DateTimeField(auto_now_add=True)
    modified =      models.DateTimeField(auto_now=True)

class Withdrawal(models.Model):
    """
    Used to collect a history of withdrawals. Only lithuanian banks for now.
    ______________________
    wallet_snapshots - user wallet before and after, to easily see changes
    initiated - when user iniated the request
    was_cleared - when I send the person money, I gotta do this.
    date_when_cleared - also set this after I send money
    """
    user =                      models.ForeignKey(User, on_delete=models.DO_NOTHING)
    amount =                    models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(10)])
    wallet_snapshot_before =    models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(10)])
    wallet_snapshot_after =     models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    was_cleared =               models.BooleanField(default=False)
    date_when_cleared =         models.DateTimeField(blank=True, null=True)
    account_number =            models.CharField(max_length=20)
    account_holder_details =    models.CharField(max_length=200)
    created =                   models.DateTimeField(auto_now_add=True)

class Payment(models.Model):
    """
    Used to collect history of payments after user pays for friend
    ___________________________
    amount_paid - total amount for how much the user paid for service
    was_disputed - if friend didn't provide service, the user can send a dispute (in 24 hour time)
    date_of_payout - 24 hours after meeting time
    """
    order =             models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    amount =            models.DecimalField(max_digits=6, decimal_places=2)
    was_disputed =      models.BooleanField(default=False)
    created =           models.DateTimeField(auto_now_add=True)
    date_of_payout =    models.DateTimeField()

class Dispute(models.Model):
    """
    For handling disputes and dealing with problematic users/friends.
    _________________________________
    report_by_user - if user or friend made the report.
    """
    class Statuses(models.IntegerChoices):
        NEW = 1, "New report"
        IN_PROGRESS = 2, "Being Reviewed"
        DISPUTED = 3, "Disputed"

    order =     models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    reported_by_user = models.BooleanField()
    message =   models.TextField(max_length=1000)
    status =    models.SmallIntegerField(choices=Statuses, default=Statuses.NEW)
    created =   models.DateTimeField(auto_now_add=True)

class Log(models.Model):
    """
    used for logging actions on website
    ________________________________
    self_explanatory
    """
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    message = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
