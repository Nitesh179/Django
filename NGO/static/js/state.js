const states = {
    AndhraPradesh:[
        "Srikakulam","Parvathipuram Manyam","Vizianagaram","Visakhapatnam","Alluri Sitharama Raju","Anakapalli","Kakinada","East Godavari","Dr. B.R. Ambedkar Konaseema","Eluru","West Godavari","NTR","Krishna","Palnadu","Guntur","Bapatla","	Prakasam",
        "Sri Potti Sriramulu Nellore","Kurnool","Nandyal","Anantapuramu","Sri Sathya Sai","YSR","Annamayya","Tirupati","Chittoor"
    ],
    ArunachalPradesh:[
        "Anjaw","Itanagar","Changlang","Dibang Valley","East Kameng","East Siang","Kra Daadi","Kurung Kumey","Lepa Rada","Lohit","Longding","Lower Dibang Valley","Lower Siang","Lower Subansiri","Namsai","Pakke Kessang","Papum Pare","SHI YOMI","Siang","Tawang","Tirap","Upper Siang","Upper Subansiri","West Kameng","West Siang"
    ],
    Assam:[
        "Baksa","Barpeta","Bongaigaon","Cachar","Charaideo","Chirang","Darrang","Dhemaji","Dhubri","Dibrugarh","Dima Hasao",
        "Goalpara","Golaghat","Hailakandi","Jorhat","Kamrup Metropolitan","Kamrup","Karbi Anglong","Karimganj","Kokrajhar",
        "Lakhimpur","Majuli","	Morigaon","Nagaon","Nalbari","Sivasagar","Sonitpur","South Salmara-Mankachar","Tinsukia","Udalguri","West Karbi Anglong"
    ],
    Bihar:[
        "Araria","Arwal","Aurangabad","Banka","Begusarai","Bhagalpur","Bhojpur","Buxar","Darbhanga","East Champaran","Gaya","Gopalganj","Jamui","Jehanabad","Khagaria","Kishanganj","Kaimur","Katihar","Lakhisarai","Madhubani","Munger","Madhepura","Muzaffarpur","Nalanda","Nawada","Patna","	Purnia","Rohtas","Saharsa","Samastipur","Sheohar","Sheikhpura","Saran","Sitamarhi","Supaul","Siwan","Vaishali","West Champaran"
    ],
    Chhattisgarh:[
        "Balod","Baloda Bazar","Balrampur","Bastar","Bemetara","Bijapur","Bilaspur","Dantewada","Dhamtari","Durg","Gariaband","Gaurella-Pendra-Marwahi","Janjgir-champa","Jashpur","Kabirdham","Kanker","Kondagaon","Khairagarh-Chhuikhadan-Gandai","Korba","Koriya","Mahasamund","Manendragarh-Chirmiri-Bharatpur","Mohla-Manpur-Chowki","Mungeli","Narayanpur","Raigarh","Raipur","Rajnandgaon","Sarangarh-Bilaigarh","Sakti","Sukma","Surguja","Surguja"
    ],
    Goa:[
       "North Goa","South Goa"
    ],
    Gujarat:[
        "Ahmedabad","Amreli","Anand","Aravalli","Banaskantha","Bharuch","Bhavnagar","Botad","Chhota Udaipur","Dahod","Dang","Devbhoomi Dwarka","Gandhinagar","Gir Somnath","Jamnagar","Junagadh","Kutch","Kheda","Mahisagar","Mehsana","Morbi","Narmada","Navsari","Panchmahal","Patan","Porbandar","Rajkot","Sabarkantha","Surat","Surendranagar","Tapi","Vadodara","Valsad"
    ],
    Haryana:[
        "Ambala","Bhiwani","Charkhi Dadri","Faridabad","Fatehabad","Gurugram","Hisar","Jhajjar","Jind","Kaithal","Karnal","Kurukshetra","Mahendragarh","Nuh","Palwal","Panchkula","Panipat","Rewari","Rohtak","Sirsa","Sirsa","Yamunanagar"
    ],
    HimachalPradesh:[
        "Bilaspur","Chamba","Hamirpur","Kangra","Kinnaur","Kullu","Lahaul and Spiti","Mandi","Shimla","Sirmaur","Solan","Una"
    ],
    Jammu_and_Kashmir:[
        	"Doda","Jammu","Kathua","Kishtwar","Poonch","Rajouri","Ramban","Reasi","Samba","Udhampur","Anantnag","Bandipora","Baramulla","Budgam","Ganderbal","Kulgam","Kupwara","Pulwama","Shopian","Srinagar","Kargil","Leh"
    ],
    Jharkhand:[
        "Bokaro","Chatra","Deoghar","Dhanbad","Dumka","East Singhbhum","Garhwa","Giridih","Godda","Gumla","Hazaribagh","Jamtara","Khunti","Kodarma","Latehar","Lohardaga","Pakur","Palamu","Ramgarh","Ranchi","Sahibganj","Saraikela Kharsawan","Simdega","West Singhbhum",""
    ],
    Karnataka:[
        "Bagalkote","Bengaluru Urban","Bengaluru Rural","Belagavi","Ballary","Bidar","Vijayapura","Chamarajanagara","Chikkaballapura","Chikkamagaluru","Chitradurga","Dakshina Kannada","Davanagere","Dharwad","Gadag","Kalaburagi","Hassan","Haveri","Kodagu","Kolara","Koppala","Mandya","Mysuru","Raichuru","Ramanagara","Shivamogga","Tumakuru","Udupi","Uttara Kannada","Vijayanagara","Yadgiri"
    ],
    Kerala:[
        "Alappuzha","Ernakulam","Idukki","Kannur","Kasaragod","Kollam","Kottayam","Kozhikode","Malappuram","Palakkad","Pathanamthitta","Thiruvananthapuram","Thrissur","Wayanad"
    ],
    MadhyaPradesh:[
        "Agar Malva","Alirajpur","Anuppur","Ashoknagar","Balaghat","Barwani","Betul","Bhind","Bhopal","Burhanpur","Chhaterpur","Chhindwara","Damoh","Datiya","Dewas","Dhar","Dindori","Guna","Gwalior","Harda","Indore","Jabalpur","Jhabua","Katni","Khandwa","Khargone","Mandla","Mandsaur","Morena","Narmadapuram","Narsingpur","Neemuch","Niwari","Panna","Raisen","Rajgarh","Ratlam","Rewa","Sagar","Satna","Sehore","Seoni","Shahdol","Shajapur","Sheopur","Shivpuri","Sidhi","Singrouli","Tikamgarh","Ujjain","Umaria","Vidisha"
    ],
    Maharashtra:[
        "Ahmednagar","Akola","Amravati","Aurangabad","Beed","Bhandara","Buldhana","Chandrapur","Dhule","Gadchiroli","Gondia","Hingoli","Jalgaon","Jalna","Kolhapur","Latur","Mumbai City","Mumbai Suburban","Nagpur","Nanded","Nandurbar","Nashik","Osmanabad","Palghar","Parbhani","Pune","Raigad","Ratnagiri","Sangli","Satara","Sindhudurg","Solapur","Thane","Wardha","Washim","Yavatmal"
    ],
    Manipur:[
        "Bishnupur","Chandel","Churachandpur","Imphal East","Imphal West","Senapati","Tamenglong","Thoubal","Ukhrul","Kangpokpi", "Tengnoupal","Pherzawl","Noney","Kamjong","Jiribam","Kakching"
    ],
    Maghalaya:[
        "East Khasi Hills","West Garo Hills","West Jaintia Hills","West Khasi Hills","East Garo Hills","Ri Bhoi","South Garo Hills","South West Garo Hills","South West Khasi Hills","East Jaintia Hills","North Garo Hills","Eastern West Khasi Hills"
    ],
    Mizoram:[
        "Aizawl","Lunglei","Siaha","Champhai","Kolasib","Serchhip","Mamit","Lawngtlai","Hnahthia","Saitual","Khawzawl"
    ],
    Nagaland:[
        "Chümoukedima","Dimapur","Kiphire","Kohima","Longleng","Mokokchung","Mon","Niuland","Noklak","Peren","Phek","Shamator", "Tuensang","Tseminyü","Wokha","Zünheboto"
    ],
    Odisha:[
        "Angul","Boudh","Balangir","Bargarh","Balasore","Bhadrak","Cuttack","Debagarh","Dhenkanal","Ganjam","Gajapati","Jharsuguda","	Jajpur","Jagatsinghapur","Khordha","Kendujhar","Kalahandi","Kandhamal","Koraput","Kendrapara","Malkangiri","Mayurbhanj","Nabarangpur","Nuapada","Nayagarh","Puri","Rayagada","Sambalpur","Subarnapur","Sundargarh"
    ],
    Panjab:[
        "Amritsar","Barnala","Bathinda","Faridkot","Fatehgarh Sahib","Firozpur","Fazilka","Gurdaspur","Hoshiarpur","Jalandhar","Kapurthala","Ludhiana","Malerkotla","Mansa","Moga","Sri Muktsar Sahib","Pathankot","Patiala","Rupnagar","Sahibzada Ajit Singh Nagar","Sangrur","Shahid Bhagat Singh Nagar","Tarn Taran"
    ],
    Rajasthan:[
        "Ajmer","Alwar","Banswara","Baran","Barmer","Bharatpur","Bhilwara","Bikaner","Bundi","Chittorgarh","Churu","Dausa","Dholpur","Dungarpur","Hanumangarh","Jaipur","Jaisalmer","Jalore","Jhalawar","Jhunjhunu","Jodhpur","Karauli","Kota","Nagaur","Pali","Pratapgarh","Rajsamand","Sawai Madhopur","Sikar","Sirohi","Sri Ganganagar","Tonk","Udaipur"
    ],
    Sikkim:[
        "	Gangtok","Mangan","Namchi","Gyalshing or Geyzing","Pakyong","Soreng"
    ],
    TamilNadu:[
        "Ariyalur","Chengalpattu","Chennai","Coimbatore","Cuddalore","Dharmapuri","Dindigul","Erode","Kallakurichi","Kanchipuram","Kanniyakumari","Karur","Krishnagiri","Madurai","Mayiladuthurai","Nagapattinam","Namakkal","Nilgiris","Perambalur","Pudukkottai","Ramanathapuram","Ranipet","Salem","Sivagangai","Tenkasi","Thanjavur","Theni","Thoothukudi","Tiruchirappalli","Tirunelveli","Tirupathur","Tiruppur","Tiruvallur","Tiruvannamalai","Tiruvarur","Vellore","Viluppuram","Virudhunagar"
    ],
    Telangana:[
        "Adilabad","Kumuram Bheem","Mancherial","Nirmal","Nizamabad","Jagitial","Peddapalli","Kamareddy","Rajanna Sircilla","Karimnagar","Jayashankar","Sangareddy","Medak","Siddipet","Jangaon","Hanamkonda","Warangal","Mulugu","Bhadradri","Khammam","Mahabubabad","Suryapet","Nalgonda","Yadadri","Medchal–Malkajgiri","Hyderabad","Ranga Reddy","Vikarabad","Narayanpet","Mahabubnagar","Nagarkurnool","Wanaparthy","Jogulamba"
    ],
    Tripura:[
        "Dhalai","Gomati","Khowai","Sipahijala","Unakoti","North Tripura","South Tripura","West Tripura"
    ],
    UttaraKhand:[
        "Almora","Bageshwar","Chamoli","Champawat","Dehradun","Haridwar","Nainital","Pauri Garhwal","Pithoragarh","Rudraprayag","Tehri Garhwal","Udham Singh Nagar","Uttarkashi"
    ],
    Uttarpradesh:[
        "Agra","Aligarh","Allahabad","Ambedkar Nagar","Amethi","Amroha","Auraiya","Azamgarh","Baghpat","Bahraich","Ball","Balrampur","Banda","Barabanki","Bareilly","Basti","Bijnor","Budaun","Bulandshahar","Chandauli","Chitrakoot","Deoria","Etah","Etawah","Faizabad","Farrukhabad","Fatehpur","Firozabad","Gautam Buddha Nagar","Ghaziabad","hazipur","Gonda","Gorakhpur","Hamirpur","Hapur","Hardoi","Hathras","Jalaun","Jaunpur","Jhansi","Kannauj","Kanpur Dehat","Kanpur Nagar","Kasganj","Kaushambi","Kushi Nagar","Lakhimpur Kheri","Lalitpur","Lucknow","Maharajganj","Mahoba","Mainpuri","Mathura","Mau","Meerut","Mirzapur","Moradabad","Muzaffarnagar","Pilibhit","Pratapgarh","Raebareli","Rampur","Saharanpur","Sambhal","Sant Kabir Nagar","Sant Ravidas Nagar","Shahjahanpur","Shamli","Shravasti","Siddharth Nagar","Sitapur","Sonbhadra","Sultanpur","Unnao","Varanasi",
    ],
    WestBengal:[
        "Alipurduar","Bankura","Paschim Bardhaman","Purba Bardhaman","Birbhum","Cooch Behar","Darjeeling","Dakshin Dinajpur","Hooghly","Howrah","Jalpaiguri","Jhargram","Kolkata","Kalimpong","Malda","Paschim Medinipur","Purba Medinipur","Murshidabad","Nadia","North 24 Parganas","South 24 Parganas","Purulia","Uttar Dinajpur"
    ]
}

export {states};