use surgery;

-- these here just for you to check your tables at the end if you want to, no need to run really --
select * from customer;
select * from patient;
select * from product;
select * from vet_personnel;
select * from order_history;

update product
set prod_image = concat(prod_image, '.png')
where product_id > 0;

update credential


-- please only run one batch at a time as they need the foreign keys --
insert into customer values(1, "Faye", "Quinn", "fayequinn@email.com", "4 Blossom Hill, WF4 6HT", "07836233821", "1");
insert into customer values(2, "Amalia", "Smith", "amaliasmith@email.com", "87 Cherry Tree Drive, WF5 6F1", "07865752816", "1");
insert into customer values(3, "Lois", "Travis", "loistravis@gmail.com", "14 Parsonage Close, M28 3PT", "07620853399", "1");
insert into customer values(4, "John", "Barnes", "jb@gmail.com", "5 The Row, BL1 5LJ", "07783888555", "1");
insert into customer values( 5, "Jenna", "Wade", "jennagirl@gmail.com", "15 Walton avenue, TS5 7RN", "07885101295", "1");
insert into customer values(6, "Amy", "Lou", "LouLou@yahoo.com", "6 Grove Crescent, L5 9TH", "07225699123", "1");
insert into customer values(7, "Silvia", "Crawford", "scrawford@tr.co.uk", "Rose Cottage, Silver avenue, LS12 1RR", "07966223692", "1");
insert into customer values(8, "Adaeze", "Atuegwu", "aasmile@gmail.com", "89 Trent Street, MK4 8LL", "", "0");
insert into customer values(9,  "Tyrone", "Taylor", "Martin.Taylors@Banksford.co.uk", "5 Cliff Terrace, LA9 4JR", "07966336926", "1");
insert into customer values(10, "John", "Bailey", "jjbai456@gmail.com", "Flat 2, Endfield Flats, WA16 7RP", "07722881810", "1");
insert into customer values(11, "Debbie", "Voce", "DVoce@gmail.com", "14 Burnley Road, BB2 4RT", "07885556996", "1");
insert into customer values(12, "Sarah", "Keene", "sarahkeene@email.com", "154 Markland Hill Lane, EH16 2DD", "07835669221", "1");
insert into customer values(13, "John", "Digby", "thedigby@email.com", "87 Cherry Tree Drive, WF5 6F1", "07826666363", "1");
insert into customer values(14,  "Harsha", "Patel", "soharsh@gmail.com", "14 Parsonage Close, M28 3PT", "07741552825", "1");

insert into patient values (1, "1", "George", "cat", "domestic cat", "m", "2020-06-01", "4500", "900074125555695", "1", "0");
insert into patient values (2, "2", "Rover", "dog", "Labradooodle", "m", "2021-05-06", "9900", "0A02589236", "1",  "1");
insert into patient values (3, "3", "Raven", "rabbit", "Mini Lop", "m", "2022-01-01", "2500", "", "0", "0");
insert into patient values (4, "4", "Patch", "cat", "Siamese", "f", "2007-10-06", "4100", "154266968", "0", "1");
insert into patient values (5, "5", "Archie", "dog", "French Bulldog", "m", "2017-06-01", "11000", "900074222335859", "1", "1");
insert into patient values (6, "5", "Spike", "dog", "Chihuahua", "m", "2018-09-22", "1900", "555698569", "1", "0");
insert into patient values (7, "7", "Teddy", "dog", "Afgan Hound", "m", "2014-06-01", "24500", "900074111524582", "0", "1");
insert into patient values (8, "7", "Button", "cat", "domestic cat", "m", "2023-01-28", "2500", "0A05528596", "1", "1");
insert into patient values (9, "9", "Leila", "cat", "domestic cat", "f", "2015-01-01", "4900", "999221552336050", "1", "1");
insert into patient values (10, "8", "Basil", "dog", "German Shepherd", "m","2015-08-05", "25000", "", "1", "1");
insert into patient values (11, "12", "Max", "dog", "Border Collie", "m", "2009-10-01", "24500", "999225126482552", "1", "0");
insert into patient values (12, "5", "Fluffy", "cat", "domestic cat", "f", "2016-01-01", "4500", "0A02258759", "1", "0");
insert into patient values (13, "10", "Midnight", "guinea pig", "", "f", "2020-10-01", "950", "", "0", "0");
insert into patient values (14, "6", "Sybil", "cat", "domestic cat", "f", "2009-09-01", "4200", "900074444685", "1", "0");
insert into patient values (15, "6", "Samson", "cat", "domestic cat", "m", "2009-09-01", "5150", "900074582999", "1", "0");
insert into patient values (16, "12", "Trent", "dog", "Border Collie", "m", "2010-10-06", "25000", "0A05552695", "1", "1");
insert into patient values (17, "13", "Nelly", "dog", "Dachshund", "f", "2020-05-09", "10200", "111635926", "1", "1");
insert into patient values (18, "14", "Socks", "cat", "Bengal", "f", "2015-01-06", "6500", "999253625986559", "1", "1");

insert into product values (1, "2859", "food", "Royal Canin Anallergenic Dry Dog Food", "Complete anallergenic dog food formulated to reduce ingredient and nutrient intolerances. 3kg bag. ", "prod1", "dog", "2");
insert into product values (2, "4495", "food", "Royal Canin Urinary S/O Cat Food ", "Royal Canin Feline Urinary S/O Morsels in Gravy Adult Wet Food is a complete dietetic feed for cats. Its urine acidifying properties and its low level of magnesium make it suitable for dissolving struvite stones and reducing their recurrence. 48x85g Pouch", "prod2", "cat", "4");
insert into product values (3, "1009", "food", "Burgess Excel Junior and Dwarf Rabbit Nuggets with Mint", "A delicious, complementary food for baby rabbits which is also perfect for dwarf rabbits. It's high in protein, fibre and rich in nutrients to help keep your rabbit strong, happy and healthy. 4kg bag", "prod3", "small animal", "10");
insert into product values (4, "949", "medication", "Imidaflea Spot-On Solution for Cats, Pet Rabbits and Dogs", "Imidaflea Spot-On Solution for Cats, Pet Rabbits and Dogs is an effective solution kills fleas, flea larvae/pupae and biting lice. It is an Imidacloprid based formula and will quickly kill fleas within 24 hours of application. Medium dogs weighing 4kg - 10kg. Pack of 3", "prod4", "dog", "20");
insert into product values (5, "229", "medication", "Milprazon Chewable Wormer Tablets for Cats", "A palatable broad spectrum wormer for cats to control and teat mixed infections by immature and adult cestodes and nematodes. Also for the prevention against heartworm and lungworm. 4mg/10mg Chewable", "prod5", "cat", "1");
insert into product values (6, "3035", "medication", "ADAPTIL Chew - Dog Calming Treats", "ADAPTIL Chew - Dog Calming Treats are a Fast Calming and Tasty bite for your Dog when facing stressful situations: loud noises like fireworks and thunderstorms, visitors, transport by car, visits to the vet, grooming sessions, dog show, etc. ", "prod6", "dog", "6");
insert into product values (7, "3675", "accessories", "Hurtta Casual Padded Y-Harness", "Hurtta Casual Padded Harness - ideal for everyday walks and activities for all dogs. The Padded Harness harness is comfortable to wear and can be easily adjusted to suit your dog. It also has efficent 3M reflectors to improve visibility in the dark. Red. 60cm", "prod7", "dog", "1");
insert into product values (8, "1320", "accessories", "SureFlap Pet Door Tunnel Extender", "SureFlap Pet Door Tunnel Extenders can be stacked together to create a longer approach tunnel to the SureFlap Microchip Pet Door or the Microchip Pet Door Connect when it is installed in a wall. This tunnel extender fits neatly onto the 70mm long tunnel of the SureFlap Pet Door and each tunnel extender adds 50mm to the overall length of the tunnel.", "prod8", "cat", "0");
insert into product values (9, "2629", "accessories", "Buster Dog Maze - Grey", "The Buster Dog Maze Food Bowl is an innovative and fun way to feed your pooch, as not only will it reduce the speed in which your dog wolfs down their lunch, but also stimulate their minds.", "prod9", "dog", "3");
insert into product values (10, "489", "toiletries", "Animology Star Pups Body Mist", "Animology Star Pups Body Mist is a fragrance body mist for dogs with long lasting notes of soft and gentle Shea and Vanilla. 230ml", "prod10", "dog", "2");
insert into product values (11, "1569", "toiletries", "Douxo S3 Pyo Mousse", "Douxo S3 Pyo Mousse is a purifying mousse for dogs: disinfects thanks to the antiseptic action of 3% chlorhexidine digluconate while hydrating and maintaining the skin’s ecosystem. Antibacterial and antifungal efficacy within 10 minutes. Helps to detangle the fur and leaves the coat soft and skin. 150ml", "prod11", "dog", "3");
insert into product values (12, "2639", "toiletries", "Enisyl-F Oral Paste for Cats", "Enisyl-F is used for treatment of Feline Herpes Virus (FHV-1). It is a palatable lysine base that comes in a unique pump for easy administration. Enisyl helps to lessen the frequency and severity of FHV-1 infections. 100ml", "prod12", "cat", "5");
insert into product values (13, "699", "toys", "Rosewood Boredom Breaker Glitter Hamster Ball", "Provides hours of fun for your precious pet. Is great for when you are giving their home a spring clean. Please note colours may vary.", "prod13", "small animal", "2");
insert into product values (14, "905", "toys", "Happy Pet Country Game Goose Dog Toy", "Happy Pet Country Game Goose Dog Toy is made from a tough canvas material with a squeak for added fun, great for long hours of throwing, catching, retrieving, this toy can also be used as a training toy for gun dogs.", "prod14", "dog", "0");
insert into product values (15, "495", "toys", "Kong Snake Teaser Cat Toy", "Kong Snake Teaser Cat Toy is perfect for fun, interactive play. Irresistible feathers and unpredictable movement will stimulate your cat friend’s natural hunting instincts and provide beneficial exercise. The Snake Teaser is sure to bring out the playful tiger in any cat. Durable and safe, this item is for supervised play only.", "prod15", "cat", "3");

insert into order_history values (1, "2", "4", "1", "2023-04-01", "1", "2023-04-06");
insert into order_history values (2, "6", "7", "1", "2023-04-03", "1", "2023-04-08");
insert into order_history values (3, "5", "7", "1", "2023-04-03", "1", "2023-04-08");
insert into order_history values (4, "15", "14", "1", "2023-04-03", "0", "2023-04-08");
insert into order_history values (5, "2", "5", "1", "2023-04-03", "1", "2023-04-08");
insert into order_history values (6, "6", "2", "2", "2023-04-07", "1", "2023-04-12");
insert into order_history values (7, "7", "12", "1", "2023-04-08", "1", "2023-04-13");
insert into order_history values (8, "14", "2", "1", "2023-04-10", "1", "2023-04-15");
insert into order_history values (9, "8", "7", "1", "2023-04-10", "1", "2023-04-15");
insert into order_history values (10, "9", "5", "2", "2023-04-11", "1", "2023-04-16");
insert into order_history values (11, "4", "6", "1", "2023-04-12", "1", "2023-04-17");
insert into order_history values (12, "2", "6", "1", "2023-04-13", "1", "2023-04-18");
insert into order_history values (13, "4", "14", "1",  "2023-04-15",  "1", "2023-04-20");
insert into order_history values (14, "10", "5", "1", "2023-04-16", "0", "2023-04-21");
insert into order_history values (15, "11", "13", "1", "2023-04-16", "0", "2023-04-21");
insert into order_history values (16, "12", "1", "1", "2023-04-16", "0", "2023-04-21");

insert into vet_personnel values (1, "Moonika", "Rauk", "surgery", "vet");
insert into vet_personnel values (2, "Peter", "James", "surgery", "vet assistant");
insert into vet_personnel values (3, "Manisha", "Rai", "admin", "reception");


   
    
    
    
    
    
    

    
    
    
	
	
	
    
   
	
    
    
    
    





    
    
    
    
    



