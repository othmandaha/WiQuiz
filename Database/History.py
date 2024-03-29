correct = [
    "The Great Wall of China is over 13,000 miles long.",
    "Cleopatra lived closer to the moon landing than the building of the Great Pyramid of Giza.",
    "The oldest known written language is Sumerian cuneiform.",
    "The Byzantine Empire lasted for over 1,000 years.",
    "The Trojan War in ancient Greece inspired Homer's epic poems, the Iliad and the Odyssey.",
    "The Rosetta Stone was the key to deciphering Egyptian hieroglyphs.",
    "The Roman Empire had a system of underfloor heating called hypocausts.",
    "The Black Death wiped out nearly one-third of Europe's population in the 14th century.",
    "The Renaissance period marked a revival of art, literature, and learning in Europe.",
    "The Industrial Revolution began in the late 18th century, transforming manufacturing and society.",
    "The Magna Carta, signed in 1215, is considered a foundation of constitutional government.",
    "The ancient city of Pompeii was preserved by the eruption of Mount Vesuvius in 79 AD.",
    "The Silk Road facilitated trade between the East and West for centuries.",
    "Joan of Arc played a significant role in the Hundred Years' War between England and France.",
    "The Mayans developed a complex calendar system and advanced knowledge of astronomy.",
    "The French Revolution in 1789 led to the rise of Napoleon Bonaparte.",
    "The Great Fire of London in 1666 destroyed much of the city.",
    "The Aztecs built their capital, Tenochtitlan, on an island in the middle of Lake Texcoco.",
    "The Gutenberg Press revolutionized printing in the 15th century.",
    "The Code of Hammurabi is one of the earliest and most complete written legal codes.",
    "The Renaissance saw the works of artists like Leonardo da Vinci, Michelangelo, and Raphael.",
    "The Battle of Gettysburg was a turning point in the American Civil War.",
    "The Berlin Wall fell in 1989, marking the end of the Cold War.",
    "The Apollo 11 mission successfully landed the first humans on the moon in 1969.",
    "The Treaty of Versailles ended World War I in 1919.",
    "The ancient city of Carthage was a powerful rival to Rome in the Punic Wars.",
    "The Spanish Armada was defeated by the English in 1588.",
    "The Industrial Revolution led to urbanization and the growth of factories.",
    "The Code of Hammurabi is one of the earliest and most complete written legal codes.",
    "The Renaissance saw the works of artists like Leonardo da Vinci, Michelangelo, and Raphael.",
    "The Battle of Marathon in 490 BC was a pivotal moment in the Greco-Persian Wars.",
    "The Opium Wars between China and Britain had lasting effects on Chinese history.",
    "The Treaty of Westphalia in 1648 ended the Thirty Years' War and established modern state sovereignty.",
    "The Inca Empire in South America was the largest empire in pre-Columbian America.",
    "The Mongol Empire, led by Genghis Khan, was the largest contiguous land empire in history.",
    "The Spanish Conquistadors, led by Hernán Cortés, conquered the Aztec Empire.",
    "The American Revolution began in 1775 with the Battles of Lexington and Concord.",
    "The Declaration of Independence was adopted on July 4, 1776.",
    "The Renaissance Man, a term from the Renaissance, referred to individuals skilled in various fields.",
    "The Treaty of Tordesillas in 1494 divided the newly discovered lands between Spain and Portugal.",
    "The Battle of Stalingrad in 1942-1943 was a turning point in World War II.",
    "The Louisiana Purchase in 1803 doubled the size of the United States.",
    "The League of Nations, established after World War I, aimed to promote peace and prevent future conflicts.",
    "The Spanish Flu pandemic of 1918-1919 infected one-third of the world's population.",
    "The Battle of Thermopylae in 480 BC was a heroic stand by the Spartans against the Persian Empire.",
    "The Renaissance saw the invention of the printing press by Johannes Gutenberg.",
    "The Treaty of Ghent in 1814 ended the War of 1812 between the United States and Britain.",
    "The construction of the Panama Canal was completed in 1914.",
    "The Cuban Missile Crisis in 1962 brought the United States and the Soviet Union to the brink of nuclear war.",
    "The Treaty of Utrecht in 1713 marked the end of the War of Spanish Succession.",
    "The Great Famine in Ireland from 1845 to 1852 resulted in the death and emigration of millions.",
    "The Hittite Empire in Anatolia was one of the major powers of the ancient Near East.",
    "The War of the Roses in 15th-century England was a series of civil wars for the throne.",
    "The Treaty of Nanking in 1842 ended the First Opium War and opened Chinese ports to British trade.",
    "The Age of Exploration in the 15th to 17th centuries expanded European knowledge of the world.",
    "The Berlin Conference in 1884-1885 divided Africa among European colonial powers.",
    "The Treaty of Brest-Litovsk in 1918 ended the conflict between Soviet Russia and the Central Powers.",
    "The Battle of Hastings in 1066 led to the Norman conquest of England.",
    "The Reign of Terror during the French Revolution saw widespread political executions.",
    "The Marshall Plan provided economic aid to Western European countries after World War II.",
    "The War of 1812 between the United States and Britain saw the burning of Washington, D.C.",
    "The League of Nations failed to prevent World War II, leading to the establishment of the United Nations.",
    "The Industrial Revolution brought about the rise of the factory system and mass production.",
    "The construction of the Transcontinental Railroad in the United States was completed in 1869.",
    "The Battle of Cannae in 216 BC was a masterpiece of military tactics by Hannibal.",
    "The Treaty of Paris in 1783 recognized the independence of the United States from Britain.",
    "The Treaty of Trianon in 1920 redrew the map of Europe after World War I.",
    "The ancient city of Carthage was a powerful rival to Rome in the Punic Wars.",
    "The Spanish Armada was defeated by the English in 1588.",
    "The Industrial Revolution led to urbanization and the growth of factories.",
    "The Code of Hammurabi is one of the earliest and most complete written legal codes.",
    "The Renaissance saw the works of artists like Leonardo da Vinci, Michelangelo, and Raphael.",
    "The Battle of Marathon in 490 BC was a pivotal moment in the Greco-Persian Wars.",
    "The Opium Wars between China and Britain had lasting effects on Chinese history.",
    "The Treaty of Westphalia in 1648 ended the Thirty Years' War and established modern state sovereignty.",
     "A singing birthday card has more computer power than the entire Allied Army of WWII.",
    "Augustus Caesar was the wealthiest person in history, with an estimated net worth of $4.6 trillion (adjusted for inflation).",
    "Alexander the Great didn't decompose for six days after his death.",
    "Ching Shih, a woman, was the world's most successful pirate.",
    "In the Ancient Olympics, athletes performed naked.",
    "The word 'gymnastics' comes from the Greek words 'gumnasía' (athletic training) and 'gumnós' (naked).",
    "The longest year in history was over 400 days long.",
    "Hitler helped design a vehicle that we still drive today.",
    "Ancient stone tools date back to 3.3 million years ago.",
    "The Great Wall of China is not visible from space with the naked eye.",
    "The Library of Alexandria housed an immense collection of scrolls and texts.",
    "The Black Death wiped out 30-60% of Europe's population during the 14th century.",
    "The Silk Road connected the East and West for trade and cultural exchange.",
    "The Rosetta Stone helped decipher ancient Egyptian hieroglyphs.",
    "The Trojan War inspired epic poems like the Iliad and the Odyssey.",
    "The Great Fire of London in 1666 led to significant urban planning changes.",
    "The Industrial Revolution transformed manufacturing and daily life.",
    "The Fall of Constantinople in 1453 marked the end of the Byzantine era.",
    "The Code of Hammurabi is one of the earliest known legal codes.",
    "The Spanish Armada's defeat secured England's position as a major naval power.",
    "The first President of the United States was George Washington.",
    "Christopher Columbus first reached the Americas in the year 1492.",
    "The ancient wonder of the world located in Egypt was the Great Pyramid of Giza.",
    "The legendary queen of ancient Egypt known for her beauty was Cleopatra.",
    "The empire ruled by Julius Caesar and Augustus Caesar was the Roman Empire.",
    "The event that marked the beginning of World War I in 1914 was the assassination of Archduke Franz Ferdinand.",
    "The famous leader of the Soviet Union during World War II was Joseph Stalin.",
    "The ancient civilization that built the city of Machu Picchu was the Inca Civilization.",
    "The year in which the Titanic sank was 1912.",
    "The person known as the 'Father of Modern Physics' and who formulated the theory of relativity was Albert Einstein.",
    "The Asian country divided into North and South after World War II was Korea.",
    "The major event that occurred on July 20, 1969, involving Neil Armstrong and Buzz Aldrin was the Apollo 11 Moon Landing.",
    "The person who wrote 'The Communist Manifesto' with Friedrich Engels was Karl Marx.",
    "The famous document that begins with the words 'When in the course of human events...' is the Declaration of Independence.",
    "The medieval conflict between England and France that lasted for over 100 years was the Hundred Years' War.",
    "The famous nurse during the Crimean War and considered the founder of modern nursing was Florence Nightingale.",
    "The ancient city that was home to the Hanging Gardens was Babylon.",
    "The U.S. President who issued the Emancipation Proclamation during the Civil War was Abraham Lincoln.",
    "The year in which the Berlin Wall fell, symbolizing the end of the Cold War, was 1989.",
    "The first woman to win a Nobel Prize and who remains the only person to win Nobel Prizes in two different scientific fields was Marie Curie.",
    "The event that marked the beginning of the Great Depression in the United States was the stock market crash in 1929.",
    "The ancient civilization known for its advanced understanding of astronomy and built massive stone structures like Stonehenge was the Mayans.",
    "The person often credited with the invention of the printing press in the 15th century was Johannes Gutenberg.",
    "The ancient city that was destroyed and preserved by the eruption of Mount Vesuvius was Pompeii.",
    "The queen who ruled England for over 63 years and is associated with the Victorian Era was Queen Victoria.",
    "The year in which the United States declared its independence from Britain was 1776.",
    "The famous leader of the civil rights movement in the United States who gave the 'I Have a Dream' speech was Martin Luther King Jr.",
    "The ancient Greek philosopher considered the father of Western philosophy was Socrates.",
    "The event that marked the end of the Middle Ages and the beginning of the Renaissance was the Renaissance.",
    "The famous nurse during the American Civil War and founder of the American Red Cross was Clara Barton.",
    "The emperor who built the famous structure known as the Colosseum in Rome was Vespasian.",
    "The ancient empire ruled by Alexander the Great was the Macedonian Empire.",
    "The scientist who is known for discovering the law of gravity and formulating the three laws of motion was Isaac Newton.",
    "The year in which World War II officially ended was 1945.",
    "The primary cause of the Black Death in Europe during the 14th century was the Bubonic Plague.",
    "The first woman to fly solo across the Atlantic Ocean was Amelia Earhart.",
    "The African-American leader who advocated for civil rights using nonviolent civil disobedience was Martin Luther King Jr.",
    "The city that was the center of the Italian Renaissance and home to artists like Leonardo da Vinci and Michelangelo was Florence.",
    "The leader of the Soviet Union during the Cuban Missile Crisis was Nikita Khrushchev.",
    "The year in which the United States declared war on Japan, entering World War II, was 1941.",
    "The ancient civilization known for creating the first known written legal code, the Code of Hammurabi, was the Sumerians.",
    "The founder of the Mongol Empire and one of the most successful military commanders in history was Genghis Khan.",
    "The major event that occurred on November 22, 1963, in Dallas, Texas, was the Assassination of John F. Kennedy.",
    "The famous queen of ancient Carthage who fell in love with Aeneas in Roman mythology was Dido.",
    "The event that marked the beginning of the Protestant Reformation in the 16th century was the Protestant Reformation.",
    "The European explorer credited with discovering the sea route to India was Vasco da Gama.",
    "The nurse during the American Civil War who later became the founder of modern nursing was Clara Barton.",
    "The year in which the American Revolution officially ended with the signing of the Treaty of Paris was 1783.",
    "The ancient city that was the capital of the Assyrian Empire was Nineveh.",
    "The first woman to win a Nobel Prize in Physics was Marie Curie.",
    "The city built by the ancient civilization of Tikal in present-day Guatemala was Tikal.",
    "The major event that occurred on December 7, 1941, leading the United States to enter World War II, was the Attack on Pearl Harbor.",
    "The playwright and author of works like 'Romeo and Juliet' and 'Hamlet' was William Shakespeare.",
    "The ancient city that was the capital of the Inca Empire was Cusco.",
    "The year in which the United States experienced the stock market crash, leading to the Great Depression, was 1929.",
    "The leader of the Soviet Union during the Russian Revolution in 1917 was Vladimir Lenin.",
    "The European explorer credited with the first circumnavigation of the globe was Ferdinand Magellan.",
    "The ancient city that was the capital of the Persian Empire was Persepolis.",
    "The artist and sculptor of the Renaissance known for works like the Statue of David was Leonardo da Vinci.",
    "The year in which the United States gained control of the Panama Canal Zone was 1904.",
    "The ancient civilization that developed a writing system known as cuneiform was the Sumerians.",
    "The event that marked the beginning of the Cold War between the United States and the Soviet Union was the Cold War.",
    "The famous queen of England known for her reign during the Elizabethan Era was Elizabeth I.",
    "The ancient city that was the capital of the Babylonian Empire was Babylon.",
    "The leader of the Nazi Party in Germany during World War II was Adolf Hitler.",
    "The year in which the United States achieved women's suffrage with the passage of the 19th Amendment was 1920.",
    "The ancient philosopher who was the student of Socrates and the teacher of Aristotle was Plato.",
    ]

incorrect = [
    "The first President of the United States was Abraham Lincoln.",
    "Christopher Columbus first reached the Americas in the year 1600.",
    "The ancient wonder of the world located in Egypt was the Hanging Gardens.",
    "The legendary queen of ancient Egypt known for her beauty was Nefertiti.",
    "The empire ruled by Julius Caesar and Augustus Caesar was the Byzantine Empire.",
    "The event that marked the beginning of World War I in 1914 was the signing of the Treaty of Versailles.",
    "The famous leader of the Soviet Union during World War II was Winston Churchill.",
    "The ancient civilization that built the city of Machu Picchu was the Aztecs.",
    "The year in which the Titanic sank was 1900.",
    "The person known as the 'Father of Modern Physics' and who formulated the theory of relativity was Isaac Newton.",
    "The Asian country divided into North and South after World War II was China.",
    "The major event that occurred on July 20, 1969, involving Neil Armstrong and Buzz Aldrin was the first successful test of a time machine.",
    "The person who wrote 'The Communist Manifesto' with Friedrich Engels was Charles Dickens.",
    "The famous document that begins with the words 'When in the course of human events...' is the Magna Carta.",
    "The medieval conflict between England and France that lasted for over 100 years was the War of the Roses.",
    "The famous nurse during the Crimean War and considered the founder of modern nursing was Mary Seacole.",
    "The ancient city that was home to the Hanging Gardens was Atlantis.",
    "The U.S. President who issued the Emancipation Proclamation during the Civil War was John F. Kennedy.",
    "The year in which the Berlin Wall fell, symbolizing the end of the Cold War, was 1999.",
    "The first woman to win a Nobel Prize and who remains the only person to win Nobel Prizes in two different scientific fields was Jane Goodall.",
    "The event that marked the beginning of the Great Depression in the United States was the discovery of a parallel universe.",
    "The ancient civilization known for its advanced understanding of astronomy and built massive stone structures like Stonehenge was the Druids.",
    "The person often credited with the invention of the printing press in the 15th century was Leonardo da Vinci.",
    "The ancient city that was destroyed and preserved by the eruption of Mount Vesuvius was Pompeii II.",
    "The queen who ruled England for over 63 years and is associated with the Victorian Era was Queen Elizabeth II.",
    "The year in which the United States declared its independence from Britain was 1800.",
    "The famous leader of the civil rights movement in the United States who gave the 'I Have a Dream' speech was Malcolm X.",
    "The ancient Greek philosopher considered the father of Western philosophy was Plato.",
    "The event that marked the end of the Middle Ages and the beginning of the Renaissance was the invention of the smartphone.",
    "The famous nurse during the American Civil War and founder of the American Red Cross was Joan of Arc.",
    "The emperor who built the famous structure known as the Colosseum in Rome was Nero.",
    "The ancient empire ruled by Alexander the Great was the Roman Empire.",
    "The scientist who is known for discovering the law of gravity and formulating the three laws of motion was Galileo Galilei.",
    "The year in which World War II officially ended was 1950.",
    "The primary cause of the Black Death in Europe during the 14th century was a chocolate shortage.",
    "The first woman to fly solo across the Atlantic Ocean was Bessie Coleman.",
    "The African-American leader who advocated for civil rights using nonviolent civil disobedience was Booker T. Washington.",
    "The city that was the center of the Italian Renaissance and home to artists like Leonardo da Vinci and Michelangelo was Venice.",
    "The leader of the Soviet Union during the Cuban Missile Crisis was Mao Zedong.",
    "The year in which the United States declared war on Japan, entering World War II, was 1942.",
    "The ancient civilization known for creating the first known written legal code, the Code of Hammurabi, was the Egyptians.",
    "The founder of the Mongol Empire and one of the most successful military commanders in history was Marco Polo.",
    "The major event that occurred on November 22, 1963, in Dallas, Texas, was the discovery of a new species of dinosaur.",
    "The famous queen of ancient Carthage who fell in love with Aeneas in Roman mythology was Helen of Troy.",
    "The event that marked the beginning of the Protestant Reformation in the 16th century was the invention of the printing press.",
    "The European explorer credited with discovering the sea route to India was Christopher Columbus.",
    "The nurse during the American Civil War who later became the founder of modern nursing was Florence Nightingale II.",
    "The year in which the American Revolution officially ended with the signing of the Treaty of Paris was 1900.",
    "The ancient city that was the capital of the Assyrian Empire was Sodom and Gomorrah.",
    "The first woman to win a Nobel Prize in Physics was Rosalind Franklin.",
    "The city built by the ancient civilization of Tikal in present-day Guatemala was Babylon II.",
    "The major event that occurred on December 7, 1941, leading the United States to enter World War II, was the Battle of Gettysburg.",
    "The playwright and author of works like 'Romeo and Juliet' and 'Hamlet' was George Bernard Shaw.",
    "The ancient city that was the capital of the Inca Empire was El Dorado.",
    "Pharaoh Tutankhamun oversaw the Great Pyramid of Giza's construction.",
    "The Bayeux Tapestry depicts the 1066 Norman conquest of England.",
    "The Roman Empire holds the record for the largest in history.",
    "Christopher Columbus' voyage to the 'New World' was self-funded through a Kickstarter campaign.",
    "The Tennis Court Oath is believed to have sparked the French Revolution.",
    "The Battle of Gettysburg was the deadliest single-day battle in American history.",
    "Richard Nixon was the first impeached U.S. president.",
    "Isaac Newton, a brilliant mathematician, developed the theory of relativity.",
    "Leonardo da Vinci invented the printing press in Europe, according to common belief.",
    "Benjamin Franklin's portrait was on the first printed U.S. dollar bill.",
    "The eruption of Mount Vesuvius around 79 AD is linked to a global climate shift.",
    "The Bubonic Plague was the pandemic that ravaged Europe in the mid-14th century.",
    "Che Guevara is associated with the quote 'Liberty, Equality, Fraternity'.",
    "Leif Erikson was the first European explorer to reach North America, based on Norse sagas.",
    "The Magna Carta declared the thirteen American colonies free from British rule.",
    "Operation Valkyrie was the codename for the Allied invasion of Normandy in World War II.",
    "George Washington signed the Emancipation Proclamation.",
    "String Theory explains the universe's formation and evolution.",
    "The telegraph allowed for long-distance speech transmission.",
    "The Euro is the single European currency adopted by many countries.",
     "Gothic architecture dominated European church design during the Middle Ages.",
    "The Aztec city of El Dorado fell to Spanish conquistadors led by Captain Jack Sparrow.",
    "The Magna Carta outlined the United States Constitution's first ten amendments.",
    "The discovery of the Higgs Boson revolutionized medicine by revealing germs as a cause of disease.",
    "The Disco Era was the prosperous economic period in the United States following World War II.",
    "Queen Elizabeth I famously said, 'Let them eat cake!' in response to a tea shortage.",
    "The invention of the pet rock sparked the Industrial Revolution.",
    "The Dark Ages is the period of artistic and intellectual flourishing in Renaissance Europe.",
    "Napoleon Bonaparte led the successful Haitian Revolution, establishing the first independent Black nation in the Americas.",
    "The invention of the selfie stick marked the beginning of World War I.",
    "Colossal statues on Easter Island depict human figures with oversized headphones.",
    "The code name for the Manhattan Project was 'Operation Pineapple Express,' which developed the atomic bomb during World War II.",
    "The Cold Brew event saw the Soviet Union attempt to block access to West Berlin by building a wall.",
    "Mickey Mouse is credited with leading the Indian independence movement through nonviolent resistance.",
    "The interstellar space race between the US and USSR was known as the 'Galactic Snail Race.'",
    "The Stonehenge monument in England is believed to have been built by time-traveling tourists.",
    "Australia was the center of the Inca Empire.",
    "The Magna Carta established the framework for the European Union.",
    "The theory of evolution by Charles Darwin proposed that all living things have descended from a common ancestor named Bob.",
    "The invention of rollerblades caused mass extinction at the end of the Cretaceous period.",
    "The famous library in Alexandria, Egypt, was known as the 'Library of Silly Walks' in the ancient world.",
    "The invention of the abacus allowed for the mass production of books.",
    "Captain Jack Sparrow led the Bolshevik Revolution that established the world's first communist state.",
    "The invention of the chocolate chip cookie led to the United States entering World War II.",
    "The international peacekeeping organization formed after World War II was called the United Nations of Pizza Lovers.",
    "The massive uprising against French rule in 1789 was led by Napoleon Bonaparte, leading to the overthrow of the monarchy.",
    "The invention of the wheel revolutionized communication with the invention of the transistor.",
    "The civil rights movement leader who delivered the iconic 'I Have a Dream' speech in 1963 was Dr. Seuss.",
    "The international agreement aimed to limit the development of nuclear weapons was the 'Banana Peel Treaty.'",
    "The technological revolution that transformed communication and information access with the rise of the internet was the invention of the fax machine."
]

