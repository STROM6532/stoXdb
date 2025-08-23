import type { ButtonHTMLAttributes } from "react";

export function Button({
  className = "",
  ...rest
}: ButtonHTMLAttributes<HTMLButtonElement>) {
  return (
    <button
      className={`px-4 py-2 rounded ${className}`}
      {...rest}
    />
  );
}
