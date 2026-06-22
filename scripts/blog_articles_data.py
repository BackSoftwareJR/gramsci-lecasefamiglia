"""Dataset articoli blog usato da build-blog-overhaul.py."""

OG_IMAGE = "https://gramsci.lecasefamiglia.it/images/Coazze%20-%20Casa%20Famiglia%20Gramsci/Sala%20da%20Pranzo%20%2B%20persone%201.avif"
IMG_BASE = "../../images/Coazze - Casa Famiglia Gramsci/"


def _paragraph(text: str) -> str:
    return f"<p>{text}</p>"


def _body(topic: str, links: str, family_angle: str, practical_angle: str) -> str:
    return (
        _paragraph(
            f"Nella vita reale delle famiglie, {topic} non e mai una scelta teorica. "
            f"Chi accompagna un genitore tra i 45 e i 65 anni deve tenere insieme emozioni, tempi di lavoro, "
            f"organizzazione tra fratelli e rispetto della persona. In una casa famiglia parliamo di ospite, casa e famiglia: "
            f"un linguaggio concreto che aiuta a evitare il tono ospedaliero e a costruire decisioni serene."
        )
        + _paragraph(
            f"{family_angle} Per questo incoraggiamo sempre un confronto chiaro tra figli ed equipe, con domande pratiche, "
            f"aspettative realistiche e un percorso condiviso. I riferimenti utili sono {links}, cosi ogni scelta resta leggibile "
            f"e non dipende da promesse generiche o da urgenze dell'ultimo momento."
        )
        + _paragraph(
            f"{practical_angle} L'obiettivo e proteggere autonomia e dignita dell'ospite, mantenendo una vita quotidiana ordinata, "
            f"relazioni significative e continuita familiare nel tempo. Quando il metodo e chiaro, la famiglia si sente meno sola "
            f"e la persona accolta vive il percorso con piu fiducia."
        )
        + _paragraph(
            "Nel concreto questo significa osservare i piccoli indicatori che spesso anticipano i problemi: "
            "variazioni dell'umore, riduzione della socialita, stanchezza nei gesti abituali, difficolta nel ritmo sonno-veglia, "
            "fragilita nell'organizzazione domestica e comunicazione familiare frammentata. Intervenire con gradualita, "
            "senza drammatizzare e senza rimandare troppo, aiuta a costruire un percorso stabile e umano."
        )
        + _paragraph(
            "Per i figli questa chiarezza operativa porta anche un beneficio emotivo: meno sensazione di correre sempre in emergenza, "
            "piu capacita di esserci in modo presente e non solo urgente. Quando la casa famiglia lavora con trasparenza, "
            "la famiglia recupera energie, comunica meglio tra fratelli e riesce a trasformare una scelta difficile in un progetto "
            "di cura condiviso, concreto e sostenibile."
        )
    )


def _article(
    slug: str,
    title: str,
    meta_title: str,
    meta_desc: str,
    category: str,
    badge: str,
    reading: str,
    keywords: str,
    hero: str,
    hero_alt: str,
    related: list[str],
    wa_text: str,
    intro: str,
    sections: list[tuple[str, str, str, str, str]],
) -> dict:
    return {
        "slug": slug,
        "title": title,
        "meta_title": meta_title,
        "meta_desc": meta_desc,
        "category": category,
        "badge": badge,
        "reading": reading,
        "keywords": keywords,
        "breadcrumb": title,
        "hero": hero,
        "hero_alt": hero_alt,
        "related": related,
        "wa_text": wa_text,
        "intro": _paragraph(intro),
        "sections": [
            {"id": sec_id, "title": sec_title, "body": _body(topic, links, family_angle, practical_angle)}
            for sec_id, sec_title, topic, family_angle, practical_angle, links in sections
        ],
    }


ARTICLE_INDEX = {
    "casa-famiglia-vs-rsa-differenze": {
        "title": "Casa famiglia vs RSA: differenze vere per la tua famiglia",
        "category": "Guida",
        "badge": "primary",
        "reading": "8 min",
        "excerpt": "Confronto concreto tra casa famiglia e RSA per scegliere con lucidita.",
    },
    "scegliere-casa-famiglia-genitori": {
        "title": "Come scegliere una casa famiglia per i genitori",
        "category": "Scelta consapevole",
        "badge": "primary",
        "reading": "9 min",
        "excerpt": "Checklist pratica su ambiente, relazione, trasparenza e continuita familiare.",
    },
    "anziani-autosufficienti-coazze": {
        "title": "Anziani autosufficienti a Coazze: quando la casa e la scelta giusta",
        "category": "Territorio",
        "badge": "accent",
        "reading": "8 min",
        "excerpt": "Segnali utili per scegliere per tempo una soluzione protetta e familiare.",
    },
    "valle-di-susa-vita-anziani": {
        "title": "Valle di Susa e qualita della vita in terza eta",
        "category": "Benessere",
        "badge": "accent",
        "reading": "8 min",
        "excerpt": "Perche territorio, ritmi e vicinanza familiare fanno la differenza ogni giorno.",
    },
    "visite-familiari-casa-famiglia": {
        "title": "Visite familiari in casa famiglia: regole, ritmo e serenita",
        "category": "Vita in casa",
        "badge": "primary",
        "reading": "8 min",
        "excerpt": "Come mantenere visite efficaci, costanti e rispettose del benessere dell'ospite.",
    },
    "costi-retta-casa-famiglia-piemonte": {
        "title": "Costi e retta in casa famiglia in Piemonte: guida chiara",
        "category": "Costi",
        "badge": "primary",
        "reading": "10 min",
        "excerpt": "Cosa include la retta e come confrontare i preventivi senza sorprese.",
    },
    "inserimento-nuovo-ospite": {
        "title": "Inserimento di un nuovo ospite: i primi 30 giorni",
        "category": "Accoglienza",
        "badge": "accent",
        "reading": "9 min",
        "excerpt": "Una guida passo passo per un ingresso graduale e rispettoso.",
    },
    "autonomia-dignita-terza-eta": {
        "title": "Autonomia e dignita nella terza eta: cosa significa davvero",
        "category": "Cura relazionale",
        "badge": "accent",
        "reading": "9 min",
        "excerpt": "Scelte quotidiane per preservare identita, ruolo e autostima dell'ospite.",
    },
    "coazze-giaveno-pinerolo-servizi": {
        "title": "Da Coazze, Giaveno e Pinerolo: servizi e vicinanza reale",
        "category": "Servizi locali",
        "badge": "primary",
        "reading": "8 min",
        "excerpt": "Distanze, servizi e organizzazione familiare: cosa valutare davvero.",
    },
    "domande-figli-casa-famiglia": {
        "title": "Le domande che i figli fanno prima della casa famiglia",
        "category": "FAQ",
        "badge": "primary",
        "reading": "10 min",
        "excerpt": "Risposte pratiche ai dubbi piu comuni dei figli prima della scelta.",
    },
}


ARTICLES = [
    _article(
        slug="casa-famiglia-vs-rsa-differenze",
        title="Casa famiglia vs RSA: differenze vere per la tua famiglia",
        meta_title="Casa famiglia vs RSA: differenze vere a Coazze",
        meta_desc="Confronto pratico tra casa famiglia e RSA: ritmi, relazioni e criteri utili per scegliere con serenita.",
        category="Guida",
        badge="primary",
        reading="8 min",
        keywords="casa famiglia anziani Coazze, differenza casa famiglia RSA, scelta genitori",
        hero="Sala da Pranzo + persone 1.avif",
        hero_alt="Ospiti in sala da pranzo in un ambiente familiare a Coazze",
        related=["scegliere-casa-famiglia-genitori", "costi-retta-casa-famiglia-piemonte", "domande-figli-casa-famiglia"],
        wa_text="Ciao%2C%20vorrei%20parlare%20delle%20differenze%20tra%20casa%20famiglia%20e%20RSA%20per%20mio%20genitore.",
        intro=(
            "Quando una madre o un padre invecchia, la domanda piu frequente e casa famiglia o RSA. "
            "La differenza non e solo nel nome: cambia il modo di vivere le giornate, la relazione con i figli e "
            "la qualita del clima umano. Se vuoi un primo orientamento puoi partire da /servizi/, /rette-e-ammissione/ e /contatti/."
        ),
        sections=[
            ("modello-vita", "1) Modello di vita: struttura o casa", "il confronto casa famiglia vs RSA", "In una casa famiglia la famiglia resta centrale.", "Per orientarti guarda anche /requisiti-autosufficienza/ e /blog/scegliere-casa-famiglia-genitori/.", "<a href='/servizi/'>servizi</a>, <a href='/rette-e-ammissione/'>rette e ammissione</a>, <a href='/contatti/'>contatti</a>"),
            ("relazioni", "2) Relazioni e qualita del legame", "la continuita delle relazioni quotidiane", "I figli non sono visitatori occasionali ma parte del patto.", "Un dialogo costante riduce ansia e senso di colpa.", "<a href='/blog/visite-familiari-casa-famiglia/'>visite familiari</a>, <a href='/blog/domande-figli-casa-famiglia/'>domande dei figli</a>, <a href='/casa-famiglia-coazze/'>casa famiglia Coazze</a>"),
            ("appropriatezza", "3) Appropriatezza della scelta", "la coerenza tra bisogno reale e soluzione", "Scegliere bene significa osservare bisogni attuali, non paure astratte.", "Con criteri chiari eviti decisioni affrettate.", "<a href='/requisiti-autosufficienza/'>requisiti autosufficienza</a>, <a href='/blog/inserimento-nuovo-ospite/'>inserimento ospite</a>, <a href='/servizi/'>servizi</a>"),
            ("costi", "4) Costi e trasparenza", "la lettura corretta della retta", "La serenita economica della famiglia e parte del benessere.", "Un preventivo chiaro previene conflitti futuri.", "<a href='/blog/costi-retta-casa-famiglia-piemonte/'>costi in Piemonte</a>, <a href='/rette-e-ammissione/'>rette</a>, <a href='/contatti/'>contatti</a>"),
            ("conclusione", "Conclusione", "la decisione finale in famiglia", "Decidere insieme rafforza tutti i soggetti coinvolti.", "Una visita conoscitiva aiuta a passare dai dubbi a una scelta concreta.", "<a href='/contatti/'>contatti</a>, <a href='/servizi/'>servizi</a>, <a href='/casa-famiglia-giaveno/'>casa famiglia Giaveno</a>"),
        ],
    ),
    _article(
        slug="scegliere-casa-famiglia-genitori",
        title="Come scegliere una casa famiglia per i genitori",
        meta_title="Come scegliere una casa famiglia per i genitori",
        meta_desc="Checklist pratica per valutare casa famiglia: ambiente, equipe, trasparenza e relazione con la famiglia.",
        category="Scelta consapevole",
        badge="primary",
        reading="9 min",
        keywords="casa famiglia anziani Coazze, scegliere casa famiglia, checklist",
        hero="Ingresso 2.avif",
        hero_alt="Ingresso accogliente della casa famiglia a Coazze",
        related=["domande-figli-casa-famiglia", "inserimento-nuovo-ospite", "casa-famiglia-vs-rsa-differenze"],
        wa_text="Buongiorno%2C%20vorrei%20una%20checklist%20per%20scegliere%20la%20casa%20famiglia%20piu%20adatta.",
        intro=(
            "Scegliere una casa famiglia e una decisione che coinvolge testa e cuore. "
            "Con metodo e domande giuste si evita la fretta e si protegge il benessere di tutta la famiglia. "
            "Prima della visita consulta /servizi/, /requisiti-autosufficienza/ e /rette-e-ammissione/."
        ),
        sections=[
            ("ambiente", "1) Osservare gli spazi con occhi concreti", "la valutazione dell'ambiente", "Guardare gli spazi aiuta a capire se la persona si sentira a casa.", "L'atmosfera quotidiana vale piu di un depliant.", "<a href='/casa-famiglia-coazze/'>Coazze</a>, <a href='/casa-famiglia-giaveno/'>Giaveno</a>, <a href='/casa-famiglia-pinerolo/'>Pinerolo</a>"),
            ("equipe", "2) Qualita dell'equipe e comunicazione", "la relazione con chi accompagna l'ospite", "La famiglia ha bisogno di referenti affidabili e coerenti.", "Risposte concrete riducono incertezza e conflitti.", "<a href='/blog/domande-figli-casa-famiglia/'>domande dei figli</a>, <a href='/blog/visite-familiari-casa-famiglia/'>visite familiari</a>, <a href='/servizi/'>servizi</a>"),
            ("trasparenza", "3) Trasparenza economica e contrattuale", "la lettura della retta", "Chiarezza sui costi protegge relazioni e sostenibilita.", "Meglio chiarire subito inclusioni ed extra.", "<a href='/rette-e-ammissione/'>rette e ammissione</a>, <a href='/blog/costi-retta-casa-famiglia-piemonte/'>costi</a>, <a href='/contatti/'>contatti</a>"),
            ("continuita", "4) Continuita familiare nel tempo", "l'organizzazione delle visite e degli aggiornamenti", "Essere presenti in modo stabile aiuta l'ospite e i figli.", "Una routine condivisa rende il percorso sostenibile.", "<a href='/blog/visite-familiari-casa-famiglia/'>visite</a>, <a href='/blog/inserimento-nuovo-ospite/'>inserimento</a>, <a href='/servizi/'>servizi</a>"),
            ("conclusione", "Conclusione", "la decisione finale", "La scelta giusta nasce da confronto e ascolto reciproco.", "Una visita senza pressione e il passo piu utile.", "<a href='/contatti/'>contatti</a>, <a href='/servizi/'>servizi</a>, <a href='/casa-famiglia-coazze/'>casa famiglia Coazze</a>"),
        ],
    ),
    _article(
        slug="anziani-autosufficienti-coazze",
        title="Anziani autosufficienti a Coazze: quando la casa e la scelta giusta",
        meta_title="Anziani autosufficienti a Coazze: guida pratica",
        meta_desc="Quando una casa famiglia a Coazze e adatta a anziani autosufficienti: segnali, benefici e percorso graduale.",
        category="Territorio",
        badge="accent",
        reading="8 min",
        keywords="casa famiglia anziani Coazze, anziani autosufficienti, prevenzione isolamento",
        hero="Spazi Comuni.avif",
        hero_alt="Spazi comuni luminosi per ospiti autosufficienti",
        related=["valle-di-susa-vita-anziani", "autonomia-dignita-terza-eta", "coazze-giaveno-pinerolo-servizi"],
        wa_text="Buongiorno%2C%20sto%20valutando%20una%20casa%20famiglia%20a%20Coazze%20per%20un%20genitore%20autosufficiente.",
        intro=(
            "Scegliere per tempo una casa famiglia, quando il genitore e ancora autosufficiente, puo prevenire isolamento e crisi improvvise. "
            "La chiave e accompagnare il cambiamento con gradualita, ascolto e rispetto. "
            "Per orientarti consulta /requisiti-autosufficienza/, /servizi/ e /contatti/."
        ),
        sections=[
            ("segnali", "1) I segnali da non ignorare", "il momento giusto per agire", "Anticipare evita decisioni in emergenza.", "Leggere i segnali quotidiani protegge tutti.", "<a href='/blog/casa-famiglia-vs-rsa-differenze/'>confronto RSA</a>, <a href='/blog/scegliere-casa-famiglia-genitori/'>come scegliere</a>, <a href='/requisiti-autosufficienza/'>requisiti</a>"),
            ("coazze", "2) Perche Coazze puo aiutare", "il valore del territorio", "La vicinanza familiare resta possibile e costante.", "Un contesto tranquillo sostiene motivazione e socialita.", "<a href='/casa-famiglia-coazze/'>Coazze</a>, <a href='/casa-famiglia-giaveno/'>Giaveno</a>, <a href='/casa-famiglia-pinerolo/'>Pinerolo</a>"),
            ("autonomia", "3) Autonomia protetta nella pratica", "il mantenimento delle capacita residue", "Il supporto proporzionato rafforza autostima e dignita.", "Routine chiare riducono ansia dei figli.", "<a href='/blog/autonomia-dignita-terza-eta/'>autonomia e dignita</a>, <a href='/servizi/'>servizi</a>, <a href='/contatti/'>contatti</a>"),
            ("ingresso", "4) Ingresso graduale e condiviso", "la preparazione del passaggio", "Coinvolgere la persona evita vissuti di imposizione.", "Un piano familiare chiaro riduce tensioni tra fratelli.", "<a href='/blog/inserimento-nuovo-ospite/'>inserimento</a>, <a href='/rette-e-ammissione/'>rette e ammissione</a>, <a href='/contatti/'>contatti</a>"),
            ("conclusione", "Conclusione", "la scelta preventiva", "Decidere prima significa scegliere meglio.", "Una visita guidata aiuta a verificare la compatibilita reale.", "<a href='/contatti/'>contatti</a>, <a href='/servizi/'>servizi</a>, <a href='/casa-famiglia-coazze/'>casa famiglia Coazze</a>"),
        ],
    ),
    _article(
        slug="valle-di-susa-vita-anziani",
        title="Valle di Susa e qualita della vita in terza eta",
        meta_title="Valle di Susa e qualita vita in terza eta",
        meta_desc="Ambiente, ritmi e rete familiare in Valle di Susa: perche il territorio migliora la qualita della vita.",
        category="Benessere",
        badge="accent",
        reading="8 min",
        keywords="casa famiglia anziani Coazze, Valle di Susa anziani, benessere territorio",
        hero="Esterno 1.avif",
        hero_alt="Esterno della casa famiglia nel contesto della Valle di Susa",
        related=["coazze-giaveno-pinerolo-servizi", "anziani-autosufficienti-coazze", "visite-familiari-casa-famiglia"],
        wa_text="Ciao%2C%20vorrei%20capire%20come%20influisce%20la%20Valle%20di%20Susa%20sulla%20vita%20quotidiana%20degli%20ospiti.",
        intro=(
            "Il territorio conta quanto la struttura. "
            "In Valle di Susa molte famiglie trovano un equilibrio concreto tra tranquillita e vicinanza ai propri cari. "
            "Per orientarti puoi partire da /casa-famiglia-coazze/, /servizi/ e /contatti/."
        ),
        sections=[
            ("ritmi", "1) Ritmi piu umani e benessere quotidiano", "il rapporto tra ambiente e salute", "Un contesto sereno riduce stress e confusione.", "Ritmi regolari migliorano sonno, appetito e relazione.", "<a href='/blog/anziani-autosufficienti-coazze/'>anziani autosufficienti</a>, <a href='/servizi/'>servizi</a>, <a href='/requisiti-autosufficienza/'>requisiti</a>"),
            ("comunita", "2) Comunita e senso di appartenenza", "il valore delle relazioni di prossimita", "La famiglia vede una quotidianita viva e non isolata.", "Appartenenza e identita restano centrali.", "<a href='/blog/visite-familiari-casa-famiglia/'>visite</a>, <a href='/casa-famiglia-coazze/'>Coazze</a>, <a href='/contatti/'>contatti</a>"),
            ("distanze", "3) Distanze realistiche per i figli", "la sostenibilita delle visite", "Vicinanza reale significa costanza possibile.", "Il percorso regge quando e compatibile con la vita lavorativa.", "<a href='/casa-famiglia-giaveno/'>Giaveno</a>, <a href='/casa-famiglia-pinerolo/'>Pinerolo</a>, <a href='/blog/coazze-giaveno-pinerolo-servizi/'>servizi locali</a>"),
            ("rete", "4) Rete di servizi e continuita", "l'organizzazione territoriale", "La famiglia ha bisogno di riferimenti chiari.", "Procedure trasparenti evitano disorientamento.", "<a href='/rette-e-ammissione/'>rette</a>, <a href='/servizi/'>servizi</a>, <a href='/blog/inserimento-nuovo-ospite/'>inserimento</a>"),
            ("conclusione", "Conclusione", "la scelta territoriale", "Territorio e casa vanno valutati insieme.", "Una visita sul posto chiarisce molto piu di una lista di pro e contro.", "<a href='/contatti/'>contatti</a>, <a href='/casa-famiglia-coazze/'>casa famiglia Coazze</a>, <a href='/servizi/'>servizi</a>"),
        ],
    ),
    _article(
        slug="visite-familiari-casa-famiglia",
        title="Visite familiari in casa famiglia: regole, ritmo e serenita",
        meta_title="Visite familiari in casa famiglia: guida utile",
        meta_desc="Come organizzare visite familiari efficaci: frequenza, comunicazione con l'equipe e gestione delle criticita.",
        category="Vita in casa",
        badge="primary",
        reading="8 min",
        keywords="casa famiglia anziani Coazze, visite familiari, relazione figli",
        hero="Sala da Pranzo + persone 2.avif",
        hero_alt="Incontro tra familiari e ospiti nella sala da pranzo",
        related=["inserimento-nuovo-ospite", "domande-figli-casa-famiglia", "autonomia-dignita-terza-eta"],
        wa_text="Buongiorno%2C%20vorrei%20capire%20come%20gestite%20le%20visite%20familiari%20nella%20vita%20quotidiana.",
        intro=(
            "Le visite familiari sono parte essenziale del benessere in casa famiglia. "
            "Il punto non e solo quante visite fare, ma come farle in modo utile e sostenibile. "
            "Per iniziare puoi consultare /servizi/, /rette-e-ammissione/ e /contatti/."
        ),
        sections=[
            ("frequenza", "1) Frequenza e qualita della presenza", "l'equilibrio tra costanza e sostenibilita", "Una presenza stabile aiuta ospite e figli.", "Meglio un ritmo realistico che una corsa discontinua.", "<a href='/blog/inserimento-nuovo-ospite/'>inserimento</a>, <a href='/servizi/'>servizi</a>, <a href='/contatti/'>contatti</a>"),
            ("dialogo", "2) Dialogo con l'equipe", "la comunicazione quotidiana", "Famiglia ed equipe devono avere un canale chiaro.", "Un referente unico evita malintesi.", "<a href='/blog/domande-figli-casa-famiglia/'>domande figli</a>, <a href='/rette-e-ammissione/'>rette</a>, <a href='/servizi/'>servizi</a>"),
            ("durante", "3) Cosa fare durante la visita", "la qualita della relazione", "Gesti semplici e ascolto valgono piu di attivita forzate.", "Evitare tensioni davanti all'ospite protegge il clima emotivo.", "<a href='/blog/autonomia-dignita-terza-eta/'>autonomia</a>, <a href='/blog/scegliere-casa-famiglia-genitori/'>come scegliere</a>, <a href='/contatti/'>contatti</a>"),
            ("criticita", "4) Gestire criticita e cambi di fase", "i momenti piu delicati", "Segnalare presto aiuta a correggere il percorso.", "Piccoli aggiustamenti evitano conflitti piu grandi.", "<a href='/blog/casa-famiglia-vs-rsa-differenze/'>confronto RSA</a>, <a href='/requisiti-autosufficienza/'>requisiti</a>, <a href='/servizi/'>servizi</a>"),
            ("conclusione", "Conclusione", "la continuita affettiva", "La famiglia resta parte della casa, non fuori dalla casa.", "Con metodo e dialogo il legame si rafforza.", "<a href='/contatti/'>contatti</a>, <a href='/servizi/'>servizi</a>, <a href='/casa-famiglia-coazze/'>casa famiglia Coazze</a>"),
        ],
    ),
    _article(
        slug="costi-retta-casa-famiglia-piemonte",
        title="Costi e retta in casa famiglia in Piemonte: guida chiara",
        meta_title="Costi casa famiglia Piemonte: guida chiara",
        meta_desc="Voci incluse nella retta, extra possibili e metodo pratico per confrontare i costi in Piemonte.",
        category="Costi",
        badge="primary",
        reading="10 min",
        keywords="casa famiglia anziani Coazze, costi retta Piemonte, confronto preventivi",
        hero="Cucina 1.avif",
        hero_alt="Cucina della casa famiglia, simbolo di quotidianita condivisa",
        related=["casa-famiglia-vs-rsa-differenze", "domande-figli-casa-famiglia", "coazze-giaveno-pinerolo-servizi"],
        wa_text="Ciao%2C%20vorrei%20capire%20meglio%20quali%20voci%20sono%20incluse%20nella%20retta%20mensile.",
        intro=(
            "Il tema economico merita chiarezza fin dall'inizio. "
            "Una cifra mensile da sola non basta: serve capire cosa include, come evolve e se e sostenibile nel tempo. "
            "Puoi approfondire da /rette-e-ammissione/, /servizi/ e /contatti/."
        ),
        sections=[
            ("incluse", "1) Cosa include davvero la retta", "la composizione del costo", "Conoscere le inclusioni tutela la famiglia.", "Le voci scritte evitano interpretazioni diverse.", "<a href='/servizi/'>servizi</a>, <a href='/rette-e-ammissione/'>rette</a>, <a href='/blog/casa-famiglia-vs-rsa-differenze/'>confronto RSA</a>"),
            ("extra", "2) Extra possibili e comunicazione", "la gestione trasparente delle spese aggiuntive", "Anticipare gli extra riduce tensioni tra fratelli.", "La trasparenza economica rafforza la fiducia.", "<a href='/blog/domande-figli-casa-famiglia/'>domande figli</a>, <a href='/contatti/'>contatti</a>, <a href='/rette-e-ammissione/'>ammissione</a>"),
            ("sostenibilita", "3) Sostenibilita nel medio periodo", "la tenuta economica nel tempo", "Una scelta sostenibile protegge la serenita familiare.", "Budget realistico e ruoli chiari prevengono conflitti.", "<a href='/blog/scegliere-casa-famiglia-genitori/'>come scegliere</a>, <a href='/casa-famiglia-coazze/'>Coazze</a>, <a href='/servizi/'>servizi</a>"),
            ("confronto", "4) Metodo per confrontare preventivi", "la comparazione oggettiva", "Con una griglia unica decidi con piu lucidita.", "Guardare solo il prezzo porta spesso fuori strada.", "<a href='/blog/coazze-giaveno-pinerolo-servizi/'>servizi locali</a>, <a href='/rette-e-ammissione/'>rette</a>, <a href='/contatti/'>contatti</a>"),
            ("conclusione", "Conclusione", "la scelta economica consapevole", "Parlare di costi e un atto di cura, non freddezza.", "Con numeri chiari la decisione diventa piu serena.", "<a href='/contatti/'>contatti</a>, <a href='/servizi/'>servizi</a>, <a href='/blog/domande-figli-casa-famiglia/'>domande figli</a>"),
        ],
    ),
    _article(
        slug="inserimento-nuovo-ospite",
        title="Inserimento di un nuovo ospite: i primi 30 giorni",
        meta_title="Inserimento nuovo ospite: primi 30 giorni",
        meta_desc="Guida operativa ai primi 30 giorni: preparazione, adattamento e comunicazione famiglia-equipe.",
        category="Accoglienza",
        badge="accent",
        reading="9 min",
        keywords="casa famiglia anziani Coazze, inserimento ospite, primo mese",
        hero="Corridoio.avif",
        hero_alt="Corridoio interno della casa famiglia durante il percorso di inserimento",
        related=["visite-familiari-casa-famiglia", "scegliere-casa-famiglia-genitori", "autonomia-dignita-terza-eta"],
        wa_text="Ciao%2C%20vorrei%20organizzare%20bene%20i%20primi%2030%20giorni%20di%20inserimento%20di%20mia%20madre.",
        intro=(
            "Il primo mese in casa famiglia e una fase delicata ma decisiva. "
            "Con preparazione, linguaggio corretto e collaborazione tra famiglia ed equipe si evita lo strappo emotivo. "
            "Per il quadro completo puoi vedere /rette-e-ammissione/, /requisiti-autosufficienza/ e /contatti/."
        ),
        sections=[
            ("pre", "1) Prima dell'ingresso", "la preparazione del passaggio", "Coinvolgere la persona riduce paure e opposizioni.", "Condividere abitudini aiuta l'equipe a personalizzare da subito.", "<a href='/blog/scegliere-casa-famiglia-genitori/'>come scegliere</a>, <a href='/servizi/'>servizi</a>, <a href='/contatti/'>contatti</a>"),
            ("prima-settimana", "2) Giorni 1-7", "l'orientamento iniziale", "Visite brevi e tono rassicurante sostengono l'adattamento.", "Un canale unico di aggiornamento evita caos familiare.", "<a href='/blog/visite-familiari-casa-famiglia/'>visite</a>, <a href='/rette-e-ammissione/'>rette</a>, <a href='/servizi/'>servizi</a>"),
            ("consolidamento", "3) Giorni 8-20", "la costruzione della routine", "La continuita quotidiana rafforza fiducia e autonomia.", "Piccoli rituali personali danno stabilita emotiva.", "<a href='/blog/autonomia-dignita-terza-eta/'>autonomia</a>, <a href='/requisiti-autosufficienza/'>requisiti</a>, <a href='/contatti/'>contatti</a>"),
            ("verifica", "4) Giorni 21-30", "la verifica condivisa", "Fare punto con la famiglia previene criticita ricorrenti.", "Obiettivi realistici aiutano tutti i soggetti coinvolti.", "<a href='/servizi/'>servizi</a>, <a href='/rette-e-ammissione/'>rette</a>, <a href='/blog/domande-figli-casa-famiglia/'>domande figli</a>"),
            ("conclusione", "Conclusione", "l'avvio del percorso stabile", "Il primo mese e inizio, non traguardo finale.", "Con metodo e ascolto il percorso diventa sostenibile.", "<a href='/contatti/'>contatti</a>, <a href='/servizi/'>servizi</a>, <a href='/casa-famiglia-coazze/'>casa famiglia Coazze</a>"),
        ],
    ),
    _article(
        slug="autonomia-dignita-terza-eta",
        title="Autonomia e dignita nella terza eta: cosa significa davvero",
        meta_title="Autonomia e dignita nella terza eta",
        meta_desc="Scelte quotidiane per proteggere autonomia e dignita della persona anziana in casa famiglia.",
        category="Cura relazionale",
        badge="accent",
        reading="9 min",
        keywords="casa famiglia anziani Coazze, autonomia dignita, cura relazionale",
        hero="Salone 1.avif",
        hero_alt="Salone comune dove ospiti e familiari condividono momenti di qualita",
        related=["anziani-autosufficienti-coazze", "visite-familiari-casa-famiglia", "domande-figli-casa-famiglia"],
        wa_text="Buongiorno%2C%20mi%20interessa%20capire%20come%20preservate%20autonomia%20e%20dignita%20degli%20ospiti.",
        intro=(
            "Autonomia e dignita sono parole decisive quando si parla di terza eta. "
            "La sfida e aiutare senza sostituire, proteggere senza infantilizzare. "
            "Per approfondire il percorso puoi consultare /servizi/, /requisiti-autosufficienza/ e /contatti/."
        ),
        sections=[
            ("autonomia", "1) Supporto proporzionato", "l'equilibrio tra aiuto e autonomia", "La famiglia vede il genitore restare protagonista.", "Piccole scelte quotidiane mantengono autostima.", "<a href='/blog/anziani-autosufficienti-coazze/'>autosufficienti</a>, <a href='/servizi/'>servizi</a>, <a href='/requisiti-autosufficienza/'>requisiti</a>"),
            ("linguaggio", "2) Linguaggio e rispetto", "il peso delle parole nella cura", "Parlare in modo adulto protegge identita e ruolo.", "Chiamare per nome e chiedere consenso e fondamentale.", "<a href='/blog/visite-familiari-casa-famiglia/'>visite</a>, <a href='/contatti/'>contatti</a>, <a href='/servizi/'>servizi</a>"),
            ("storia", "3) Continuita biografica", "la storia personale dell'ospite", "Famiglia ed equipe costruiscono continuita insieme.", "Oggetti, abitudini e memoria sostengono orientamento.", "<a href='/blog/inserimento-nuovo-ospite/'>inserimento</a>, <a href='/casa-famiglia-coazze/'>Coazze</a>, <a href='/servizi/'>servizi</a>"),
            ("alleanza", "4) Alleanza con i figli", "la collaborazione nel tempo", "Confronti regolari riducono attriti e paure.", "Obiettivi condivisi rendono piu stabile il percorso.", "<a href='/blog/domande-figli-casa-famiglia/'>domande figli</a>, <a href='/rette-e-ammissione/'>rette</a>, <a href='/contatti/'>contatti</a>"),
            ("conclusione", "Conclusione", "la cura relazionale concreta", "Autonomia e dignita si costruiscono ogni giorno.", "Una casa famiglia deve rendere questo principio operativo.", "<a href='/contatti/'>contatti</a>, <a href='/servizi/'>servizi</a>, <a href='/casa-famiglia-coazze/'>casa famiglia Coazze</a>"),
        ],
    ),
    _article(
        slug="coazze-giaveno-pinerolo-servizi",
        title="Da Coazze, Giaveno e Pinerolo: servizi e vicinanza reale",
        meta_title="Coazze, Giaveno, Pinerolo: servizi utili",
        meta_desc="Come valutare servizi e distanze tra Coazze, Giaveno e Pinerolo per una scelta sostenibile.",
        category="Servizi locali",
        badge="primary",
        reading="8 min",
        keywords="casa famiglia anziani Coazze, servizi locali, Giaveno Pinerolo",
        hero="Esterno 3.avif",
        hero_alt="Esterno della casa famiglia ben collegata al territorio",
        related=["valle-di-susa-vita-anziani", "costi-retta-casa-famiglia-piemonte", "scegliere-casa-famiglia-genitori"],
        wa_text="Buongiorno%2C%20arriviamo%20da%20Giaveno%20e%20Pinerolo.%20Ci%20interessa%20capire%20servizi%20e%20vicinanza.",
        intro=(
            "La scelta di una casa famiglia deve reggere nel tempo. "
            "Per questo, oltre alla qualita interna, vanno valutate distanze reali, logistica e organizzazione delle visite. "
            "Per orientarti vedi /casa-famiglia-coazze/, /servizi/ e /contatti/."
        ),
        sections=[
            ("distanza", "1) Distanza reale e continuita", "la sostenibilita delle visite", "Una distanza gestibile permette presenza vera.", "La famiglia resta parte attiva della quotidianita.", "<a href='/casa-famiglia-giaveno/'>Giaveno</a>, <a href='/casa-famiglia-pinerolo/'>Pinerolo</a>, <a href='/casa-famiglia-coazze/'>Coazze</a>"),
            ("servizi", "2) Servizi e chiarezza operativa", "la qualita dell'organizzazione", "Figli ed equipe hanno bisogno di regole semplici.", "Informazioni chiare riducono stress e fraintendimenti.", "<a href='/servizi/'>servizi</a>, <a href='/rette-e-ammissione/'>rette</a>, <a href='/contatti/'>contatti</a>"),
            ("famiglia", "3) Impatto sull'equilibrio familiare", "la distribuzione dei ruoli", "Con ruoli condivisi la scelta e piu sostenibile.", "Il carico non deve ricadere su una sola persona.", "<a href='/blog/scegliere-casa-famiglia-genitori/'>come scegliere</a>, <a href='/blog/costi-retta-casa-famiglia-piemonte/'>costi</a>, <a href='/blog/visite-familiari-casa-famiglia/'>visite</a>"),
            ("visita", "4) Come fare una visita utile", "la valutazione sul campo", "Una visita guidata chiarisce quello che online non si vede.", "Domande pratiche rendono la scelta piu oggettiva.", "<a href='/contatti/'>contatti</a>, <a href='/servizi/'>servizi</a>, <a href='/requisiti-autosufficienza/'>requisiti</a>"),
            ("conclusione", "Conclusione", "la scelta territoriale concreta", "Territorio e qualita interna vanno letti insieme.", "Il percorso funziona se resta sostenibile per tutti.", "<a href='/contatti/'>contatti</a>, <a href='/casa-famiglia-coazze/'>casa famiglia Coazze</a>, <a href='/servizi/'>servizi</a>"),
        ],
    ),
    _article(
        slug="domande-figli-casa-famiglia",
        title="Le domande che i figli fanno prima della casa famiglia",
        meta_title="Domande dei figli prima della casa famiglia",
        meta_desc="Le domande piu frequenti dei figli prima della scelta: momento giusto, costi, visite e qualita della casa.",
        category="FAQ",
        badge="primary",
        reading="10 min",
        keywords="casa famiglia anziani Coazze, domande figli, scelta casa famiglia",
        hero="Camera 1.avif",
        hero_alt="Camera confortevole per ospiti in casa famiglia",
        related=["scegliere-casa-famiglia-genitori", "costi-retta-casa-famiglia-piemonte", "casa-famiglia-vs-rsa-differenze"],
        wa_text="Ciao%2C%20vorrei%20fare%20alcune%20domande%20prima%20di%20scegliere%20la%20casa%20famiglia%20per%20mio%20padre.",
        intro=(
            "Le domande dei figli sono il punto di partenza migliore per una scelta consapevole. "
            "Quando i dubbi vengono affrontati con chiarezza, la decisione diventa piu stabile e serena. "
            "Per partire consulta /servizi/, /rette-e-ammissione/ e /contatti/."
        ),
        sections=[
            ("momento", "1) E il momento giusto?", "la tempistica della scelta", "Rimandare troppo spesso aumenta stress e urgenza.", "Valutare presto permette una decisione piu condivisa.", "<a href='/blog/anziani-autosufficienti-coazze/'>autosufficienti</a>, <a href='/requisiti-autosufficienza/'>requisiti</a>, <a href='/contatti/'>contatti</a>"),
            ("qualita", "2) Come capisco se la casa e valida?", "i criteri di valutazione", "Le famiglie hanno bisogno di evidenze concrete.", "Atmosfera, linguaggio e coerenza dicono molto.", "<a href='/blog/scegliere-casa-famiglia-genitori/'>come scegliere</a>, <a href='/servizi/'>servizi</a>, <a href='/casa-famiglia-coazze/'>Coazze</a>"),
            ("costi", "3) Quanto costa davvero?", "la trasparenza economica", "Capire la retta evita tensioni tra fratelli.", "Con numeri chiari la decisione e piu serena.", "<a href='/blog/costi-retta-casa-famiglia-piemonte/'>costi</a>, <a href='/rette-e-ammissione/'>rette</a>, <a href='/contatti/'>contatti</a>"),
            ("presenza", "4) Resteremo presenti nella sua vita?", "il ruolo dei figli dopo l'ingresso", "La famiglia resta centrale anche dopo la scelta.", "Visite regolari e comunicazione rendono tutto piu umano.", "<a href='/blog/visite-familiari-casa-famiglia/'>visite</a>, <a href='/blog/inserimento-nuovo-ospite/'>inserimento</a>, <a href='/servizi/'>servizi</a>"),
            ("conclusione", "Conclusione", "dai dubbi alla decisione", "Fare domande e un atto di responsabilita.", "Confronto e ascolto aiutano a scegliere meglio.", "<a href='/contatti/'>contatti</a>, <a href='/servizi/'>servizi</a>, <a href='/blog/casa-famiglia-vs-rsa-differenze/'>confronto RSA</a>"),
        ],
    ),
]
