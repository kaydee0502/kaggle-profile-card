from styles import tier_colour
from badges import badge

class KaggleStyles:
   
    def present(self,data):
        
        
        style = """<style>
                    @import url(https://fonts.googleapis.com/css2?family=Inter);
                    @keyframes currstreak {
                        0% { font-size: 3px; opacity: 0.2; }
                        80% { font-size: 34px; opacity: 1; }
                        100% { font-size: 28px; opacity: 1; }
                    }
                    @keyframes fadein {
                        0% { opacity: 0; }
                        100% { opacity: 1; }
                    }
                </style>"""
        
        
        return f"""

       


            <svg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' style='isolation:isolate' viewBox='0 0 495 195' width='495px' height='195px'>
                    {style}
                    <defs>
                        <clipPath id='_clipPath_OZGVUqgkTHHpPTYeqOmK3uLgktRVSwWw'>
                            <rect width='495' height='195'/>
                        </clipPath>
                    </defs>

               


                    <g xmlns="http://www.w3.org/2000/svg" style="isolation:isolate">
                        <path d="M 4.5 0 L 490.5 0 C 492.984 0 495 2.016 495 4.5 L 495 190.5 C 495 192.984 492.984 195 490.5 195 L 4.5 195 C 2.016 195 0 192.984 0 190.5 L 0 4.5 C 0 2.016 2.016 0 4.5 0 Z" style="stroke: #e4e2e2; fill: #fffefe;stroke-miterlimit:10;rx: 4.5;"/>
                    </g>
                    

                    <g xmlns="http://www.w3.org/2000/svg" transform="translate(1,48)">
                    
                    <text x="20" y="-12" dominant-baseline="middle" stroke-width="0" style="font-family: Roboto, system-ui, sans-serif;font-weight:700;font-size:22px;font-style:normal;fill:{tier_colour[data["performanceTier"]]};stroke:none; opacity: 0; animation: fadein 0.5s linear forwards 0.6s;">
                        {data["displayName"]}
                    </text>

                     <text x="20" y="22" dominant-baseline="middle" stroke-width="0" style="font-family: Roboto, system-ui, sans-serif;font-weight:500;font-size:14px;font-style:normal;fill:#151515;stroke:none; opacity: 0; animation: fadein 0.5s linear forwards 0.6s;">
                        {"" if not data["occupation"] or not data["organization"] else data["occupation"]+" at " + data["organization"]}
                    </text>

                    <text x="20" y="40" dominant-baseline="middle" stroke-width="0" style="font-family: Roboto, system-ui, sans-serif;font-weight:500;font-size:14px;font-style:normal;fill:#151515;stroke:none; opacity: 0; animation: fadein 0.5s linear forwards 0.6s;">
                        {"" if not data["country"] else data["country"]}{"" if not data["region"] else ", "+data["region"]}{"" if not data["city"] else ", " + data["city"]}
                    </text>
                   

                   <text x="20" y="68" dominant-baseline="middle" stroke-width="0" style="font-family: Roboto, system-ui, sans-serif;font-weight:500;font-size:16px;font-style:normal;fill:#757678;stroke:none; opacity: 0; animation: fadein 0.5s linear forwards 0.6s;">
                        Followers : {data["followers"]["count"]}
                    </text>
                    <text x="20" y="86" dominant-baseline="middle" stroke-width="0" style="font-family: Roboto, system-ui, sans-serif;font-weight:500;font-size:16px;font-style:normal;fill:#757678;stroke:none; opacity: 0; animation: fadein 0.5s linear forwards 0.6s;">
                        Following : {data["following"]["count"]}
                    </text>
                </g>
                
               <g xmlns="http://www.w3.org/2000/svg" transform="translate(20.000000,185.000000) scale(0.050000,-0.05)" fill="#ad7615" stroke="none">
                <circle xmlns="http://www.w3.org/2000/svg" cx="250" cy="270" r="250"  style="fill:#ffd448;opacity: 0; animation: fadein 0.5s linear forwards 0.4s;"/>
                <path d="M170 515 c-103 -33 -170 -128 -170 -243 0 -73 15 -114 60 -166 152                 -172 440 -63 440 166 0 99 -44 175 -127 220 -62 34 -142 43 -203 23z m172 -71                 l31 -16 -134 -134 c-74 -74 -137 -134 -141 -134 -17 0 -38 62 -38 110 0 62 18                 106 58 143 59 57 150 69 224 31z"/>
                
                </g>
                
                <g xmlns="http://www.w3.org/2000/svg" transform="translate(200.000000,185.000000) scale(0.050000,-0.05)" fill="#838280" stroke="none">
                <circle xmlns="http://www.w3.org/2000/svg" cx="250" cy="270" r="250"  style="fill:#e9e9e9;opacity: 0; animation: fadein 0.5s linear forwards 0.4s;"/>
                <path d="M170 515 c-103 -33 -170 -128 -170 -243 0 -73 15 -114 60 -166 152                 -172 440 -63 440 166 0 99 -44 175 -127 220 -62 34 -142 43 -203 23z m172 -71                 l31 -16 -134 -134 c-74 -74 -137 -134 -141 -134 -17 0 -38 62 -38 110 0 62 18                 106 58 143 59 57 150 69 224 31z"/>
                </g>
                <g xmlns="http://www.w3.org/2000/svg" transform="translate(380.000000,185.000000) scale(0.050000,-0.05)" fill="#8e5b3d" stroke="none">
                <circle xmlns="http://www.w3.org/2000/svg" cx="250" cy="270" r="250"  style="fill:#f0ba7c;opacity: 0; animation: fadein 0.5s linear forwards 0.4s;"/>
                <path d="M170 515 c-103 -33 -170 -128 -170 -243 0 -73 15 -114 60 -166 152                 -172 440 -63 440 166 0 99 -44 175 -127 220 -62 34 -142 43 -203 23z m172 -71                 l31 -16 -134 -134 c-74 -74 -137 -134 -141 -134 -17 0 -38 62 -38 110 0 62 18                 106 58 143 59 57 150 69 224 31z"/>
                </g>
                
                
                
                
                <g xmlns="http://www.w3.org/2000/svg" transform="translate(40,185)">
                    
                    <text x="20" y="-12" dominant-baseline="middle" stroke-width="0" style="font-family: Roboto, system-ui, sans-serif;font-weight:700;font-size:16px;font-style:normal;fill:#ad7615;stroke:none; opacity: 0; animation: fadein 0.5s linear forwards 0.6s;">
                        {self.medalCounts(data,type="gold")}
                    </text>

                     <text x="200" y="-12" dominant-baseline="middle" stroke-width="0" style="font-family: Roboto, system-ui, sans-serif;font-weight:700;font-size:16px;font-style:normal;fill:#838280;stroke:none; opacity: 0; animation: fadein 0.5s linear forwards 0.6s;">
                       {self.medalCounts(data,type="silver")}
                    </text>

                    <text x="380" y="-12" dominant-baseline="middle" stroke-width="0" style="font-family: Roboto, system-ui, sans-serif;font-weight:700;font-size:16px;font-style:normal;fill:#8e5b3d;stroke:none; opacity: 0; animation: fadein 0.5s linear forwards 0.6s;">
                       {self.medalCounts(data,type="bronze")}
                    </text>
                   

                  
                </g>
                
                {badge[data["performanceTier"]]}
                
                <g xmlns="http://www.w3.org/2000/svg" transform="translate(392,120)">
                
                 
                    <text x="0" y="0" word-spacing="-0.2" dominant-baseline="middle" text-anchor="middle" stroke-width="0" style="font-family:sans-serif;font-weight:400;font-size:14px;font-style:normal;fill:{tier_colour[data["performanceTier"]]};stroke:none; opacity: 0; animation: fadein 0.5s linear forwards 0.6s;">
                        {"Kaggle" if data["performanceTier"]=="staff" else data["performanceTierCategory"].title()}
                    </text>
                 <text x="0" y="16" word-spacing="-0.2" dominant-baseline="middle" text-anchor="middle" stroke-width="0" style="font-family:sans-serif;font-weight:400;font-size:14px;font-style:normal;fill:{tier_colour[data["performanceTier"]]};stroke:none; opacity: 0; animation: fadein 0.5s linear forwards 0.6s;">
                        {"Team" if data["performanceTier"]=="staff" else data["performanceTier"].title()}
                    </text>
                </g>
                

            <!--<g xmlns="http://www.w3.org/2000/svg" style="isolation:isolate" transform="scale(2.5)"><circle r="22.5" cx="24" cy="24" fill="url(#profileimg)" stroke-width="3" style="stroke: rgb(241, 243, 244);"/><path d="M 10.774831823419357 42.20288237343632 A 22.5 22.5 0 1 0 24 1.5" fill="none" style="stroke: rgb(101, 31, 255);" stroke-width="3"/></g>-->

                </svg>


            """
    
    def medalCounts(self,data,type = None):
        """
        Count the current total medals from each tier.
        
        Arguements
        ----------
        data : Kaggle data in Dictionary format
        type : defines the medal type.
        
        Return
        ------
        count : count of total medal of a certain type.
        """
        
        if not type:
            return 0
        
        sections = ["competitionsSummary", "scriptsSummary", "discussionsSummary", "datasetsSummary"]
        types = {"gold" : "totalGoldMedals", "silver" : "totalSilverMedals", "bronze" : "totalBronzeMedals"}

        count = 0

        for section in sections:
            count += data[section][types[type]]
            
        return count