import media
import fresh_tomatoes

little_china = media.Movie("Big Trouble in Little China", "An All-American trucker gets dragged into a centuries-old mystical battle in Chinatown", "https://upload.wikimedia.org/wikipedia/en/7/76/Big_Trouble_in_Little_China_Film_Poster.jpg", "https://www.youtube.com/watch?v=592EiTD2Hgo")  # noqa

alien = media.Movie("Alien", "A merciless horror stalks the crew of a deep-space freighter.", "http://t2.gstatic.com/images?q=tbn:ANd9GcRGWyg4tnCNzaiUna7JSzV3I8NcwMaFhpulr1iWSd0FwW-r_89e", "https://www.youtube.com/watch?v=LjLamj-b0I8")  # noqa

blade_runner = media.Movie("Blade Runner", "A detective hunts obsolete androids in 2019.", "https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg", "https://www.youtube.com/watch?v=eogpIG53Cis")  # noqa

the_revenant = media.Movie("The Revenant", "While exploring the uncharted wilderness in 1823, legendary frontiersman Hugh Glass sustains injuries from a brutal bear attack. When his hunting team leaves him for dead, Glass must utilize his survival skills to find a way back home to his beloved family. Grief-stricken and fueled by vengeance, Glass treks through the wintry terrain to track down John Fitzgerald, the former confidant who betrayed and abandoned him.", "http://t1.gstatic.com/images?q=tbn:ANd9GcS5yuCSZqK5Hha5lElqZr2SCYVY-sYycKZ8PJ8POfNQkOmSuo5B", "https://www.youtube.com/watch?v=LoebZZ8K5N0")  # noqa

lives_of_others = media.Movie("The lives of others", "In 1984 East Berlin, an agent of the secret police, conducting surveillance on a writer and his lover, finds himself becoming increasingly absorbed by their lives.", "http://www.gstatic.com/tv/thumb/dvdboxart/163183/p163183_d_v8_aa.jpg", "https://www.youtube.com/watch?v=n3_iLOp6IhM")  # noqa

the_thing = media.Movie("The Thing", "The stage is set for havoc and terror when a 12-man research team finds an alien being that has fallen from the sky and has been buried for over 100,000 years.", "https://upload.wikimedia.org/wikipedia/en/c/c1/ThingPoster.jpg", "https://www.youtube.com/watch?v=5ftmr17M-a4")  # noqa

movies = [little_china, the_thing, lives_of_others, blade_runner, the_revenant, alien]  # noqa
fresh_tomatoes.open_movies_page(movies)
