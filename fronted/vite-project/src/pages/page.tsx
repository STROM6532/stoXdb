import { Button } from "@/components/ui/button";

const navigationItems = [
  { label: "Home", href: "#" },
  { label: "About", href: "#" },
];

export const Desktop = (): JSX.Element => {
  return (
    <div className="bg-transparent grid justify-items-center [align-items:start] w-screen">
      <div className="overflow-hidden border border-solid border-[#1e2a4466] bg-[linear-gradient(0deg,rgba(15,28,43,1)_0%,rgba(15,28,43,1)_100%),linear-gradient(0deg,rgba(10,21,34,1)_0%,rgba(10,21,34,1)_100%)] w-[1440px] h-[1024px] relative">
        <img
          className="absolute w-full h-full top-0 left-0 object-cover"
          alt="Whatsapp image"
          src="/whatsapp-image-2025-08-21-at-23-13-55-83d4a8f2-1.png"
        />

        <header className="relative z-10 flex justify-between items-center w-full h-[109px] px-12 pt-[46px]">
          <div className="[font-family:'Inter',Helvetica] font-semibold text-[#cfe8ff] text-[64px] tracking-[0] leading-[normal]">
            StoXdb
          </div>

          <nav className="flex items-center gap-12">
            {navigationItems.map((item, index) => (
              <a
                key={index}
                href={item.href}
                className="[font-family:'Inter',Helvetica] font-medium text-[#cfe8ff] text-[25px] hover:opacity-80 transition-opacity"
              >
                {item.label}
              </a>
            ))}
          </nav>
        </header>

        <main className="relative z-10 flex flex-col items-center justify-center min-h-[calc(100vh-200px)] px-6">
          <div className="text-center space-y-8">
            <div className="space-y-4">
              <h1 className="[font-family:'Inter',Helvetica] font-semibold text-white text-[80px] tracking-[0] leading-[normal]">
                Welcome to
              </h1>

              <div className="[font-family:'Inter',Helvetica] font-extrabold text-[150px] tracking-[0] leading-[normal]">
                <span className="text-[#6fd2ff]">Sto</span>
                <span className="text-[#cfe8ff]">X</span>
                <span className="text-[#6fd2ff]">db</span>
              </div>
            </div>

            <p className="[font-family:'Inter',Helvetica] font-extrabold text-[#6fd2ff] text-5xl tracking-[0] leading-[normal] mt-16">
              Your AI-powered Stock Analytics Tool
            </p>
          </div>

          <Button className="mt-16 w-[379px] h-[98px] rounded-3xl border-[1.5px] border-solid border-black shadow-[0px_0px_15px_2px_#000000] bg-[linear-gradient(0deg,rgba(64,191,255,1)_0%,rgba(64,191,255,1)_100%),linear-gradient(0deg,rgba(111,210,255,1)_0%,rgba(111,210,255,1)_100%)] [font-family:'Inter',Helvetica] font-medium text-black text-[58px] hover:opacity-90 transition-opacity h-auto">
            Get Started
          </Button>
        </main>
      </div>
    </div>
  );
};
