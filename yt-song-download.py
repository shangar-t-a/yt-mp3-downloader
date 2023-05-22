from youtube_search import YoutubeSearch
from pytube import YouTube
import os


def search_youtube_and_download(song_name):
    try:
        results = YoutubeSearch(song_name, max_results=1).to_dict()
        if results:
            video_url = "https://www.youtube.com/watch?v=" + results[0]["id"]
            print(f"Top search result for '{song_name}' found on YouTube")
            print(f"URL: {video_url}")
            confirmation = input("Do you want to download it? (y/n): ")
            if confirmation.lower() == "y":
                download_youtube_video(video_url, song_name)
            else:
                print(f"Skipping download for '{song_name}'.")
                print("*" * 150)
        else:
            print(f"No search results found for '{song_name}'.")
    except Exception as e:
        print(f"Error: {str(e)}")


def download_youtube_video(url, song_name):
    yt = YouTube(url)

    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    # check for destination to save file
    destination = r"F:\Shangar\temp\songs"

    # download the file
    out_file = video.download(output_path=destination, filename=song_name)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)

    # result of success
    print(yt.title + " has been successfully downloaded.")
    print("*" * 150)


if __name__ == "__main__":
    # Example usage
    song_names = [
        "Ennavale Adi Ennavale Song",
        "Uyirum Neeyae Song",
        "Thenmerku Paruva Kaatru Song",
        "Maharajanodu Song",
        "Meenamma Athikalaiyilum Song",
        "Pulveli Pulveli (Male) Song",
        "Tharai Varamal Song",
        "Allah Un Aanai Song",
        "Kadhali Nee Enna Seivai Song",
        "Aathukkulla Ayyarathu Ponnu Song",
        "Naalai Ulagam Song",
        "Oru Pattu Thamarai Song",
        "Anantham Anantham Female Song",
        "Machinichi Varra Neram Song",
        "Kiss Me Miss Song",
        "Sakiye Nee Thaan Song",
        "Kaalamellam Kadhal Song",
        "O Vennila Song",
        "Thendrale Song",
        "Narumugaye Narumugaye Song",
        "Yen Pen Endru Song",
        "Veesum Kaatrukku Song",
        "Mayilu Mayilu Mayilamma Song",
        "Manam Virumbuthae Male Song",
        "Sonia Sonia Song",
        "Vellipani Malarae Song",
        "Nandri Solla Unaku Song",
        "Oru Poo Ezhuthum Kavithai Song",
        "Butterfly Pattu Poo Song",
        "Super Pattu Song",
        "Kanave Kalaiyadhe Song",
        "Sola Kaattu Pathayila Song",
        "Malligai Poovae Song",
        "Bharathikku Kannamma Song",
        "Enake Enaka Song",
        "Poovukkul Olinthirukkum Song",
        "Chinna Chinna Malar Song",
        "Selaiyila Veedu Kattava Song",
        "Indha Kadhal Song",
        "Oru Thulir Song",
        "Thirakkadha Song",
        "Innisai Paadi Varum Song",
        "Innisai Padi Varum Climax Song",
        "Nadodi Nanba Song",
        "Kolusu Konjum Paadham Song",
        "Kannai Parikkira Song",
        "Antha Vaanukku Song",
        "Nilavai Konduva Song",
        "April Madhathil Song",
        "Manase Manase Kathavai Thira Song",
        "Roja Roja Song",
        "Margazhi Thingal Allava Song",
        "Margazhi Maasathu Malligai Song",
        "Enna Idhu Song",
        "Athikaalaiyil Sevalai Song",
        "Gnyapagam Irukkudha Song",
        "Ooty Malai Roja Chediyil Song",
        "Kulirudhu Kulirudhu Song",
        "Aasai Aasai Aasai Song",
        "Kadhal Neethana Song",
        "Maalai En Vethanai Song",
        "Sikaadha Sitrondru Song",
        "Nenachu Nenachu Song",
        "Poove Poove (Male Version) Song",
        "Oh Senyoreeta Song",
        "Ninaitha Varam Song",
        "Roja Poonthottam Song",
        "Enthen Kuyil Enge Song",
        "Naane Nee Nee Song",
        "Chinna Chinna Kanavugal Barama Song",
        "Poo Virinchachu Song",
        "Gayathiri Ketkum Song",
        "Vaa Vaa En Thalaiva Song",
        "Penkiliye Penkiliye Song",
        "Oh Vennila Song",
        "Unnai Kodu Ennai Tharuven Song",
        "Mamarathula Oonjal Song",
        "Vaada Vaa Song",
        "Idam Tharuvaya Song",
        "Kannukullae Unnai Vaithen Song",
        "Adi Kadhal Oru Kannil Song",
        "Enakena Yerkanave Song",
        "Kaatre En Vaasal Song",
        "En Idhayam Song",
        "Azhage Azhage Song",
        "Oru Roja Thottam Song",
        "Anbe Anbe Song",
        "Ovvoru Padalilum Song",
        "Ivan Yaaro Ivan Yaaro Song",
        "Vidaikodu Vidaikodu Song",
        "Ye Asainthadum Song",
        "Thirumba Thirumba Parthu Song",
        "Un Perai Sonnale Song",
        "Pallanguzhiyin Vattam Parthen Song",
        "Un Samayal Arayil Song",
        "Or Aayiram Yaanai Song",
        "Mercury Mele Song",
        "Mudhalam Sandhippil Song",
        "Putham Pudhu Rojaave Song",
        "Kannukkulle Kadhala Song",
        "Adi Anarkali Song",
        "Mudhal Muthalai Song",
        "Theenda Theenda (Duet) Song",
        "Happy New Year Song",
        "Sil Sil Sil Silala Song",
        "Pombalainga Kadhal Song",
        "Appadi Pakrathuna Song",
        "Nee Malara Malara Song",
        "Paarkadha Podhu Podhu Song",
        "Vaanam Adhirave Song",
        "Theendi Theendi Song",
        "Sonnalum Song",
        "Enna Nenacha Nee Song",
        "Muppadhu Nimidam Song",
        "Nenjodu Kalanthidu Song",
        "Mainave Mainave Song",
        "Thaayarum Ariyaamal Song",
        "Agap Porula Song",
        "Kalayil Dhinamum Song",
        "Anbu Alaipayuthe Song",
        "Mazhai Mazhai Song",
        "Sudum Nilavu Sudatha Song",
        "Kungumam Kalainthathe Song",
        "Pallaandu Pallaandu Song",
        "Vaarayo Vaarayo Song",
        "Kangalae Kamalalayam Song",
        "Vaan Mazhaiyin Thuligal Song",
        "Kadhal Veesum Song",
        "Oorellaam Unnai Kandu Song",
    ]

    for song_name in song_names:
        search_youtube_and_download(song_name)
